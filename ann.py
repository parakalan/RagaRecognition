import os
import pickle
import nanopq
import random
import numpy as np
from collections import namedtuple

PQModelHolder = namedtuple(
    'PQModelHolder', (
        'pq_model',
        'pq_codes',
        'indexed_data'
    )
)


class PQModelANN():
    """
     Model abstraction for approximate nearest neighbour (ANN) using Product Quantization
    """
    def __init__(self, **kwargs):
        self.minimum_required = kwargs.get("minimum_required", 5)
        self.m = kwargs.get("m", 10)
        self.ks_max = kwargs.get("ks_max", 64)
        self.n_iter = kwargs.get("n_iter", 40)
        self.filename = kwargs.get("filename", "pq_table_holder.pickle")
        self.indexed_data = kwargs.get("indexed_data", None)
        self.model = None

    def load(self, export_path: str):
        model_path = os.path.join(export_path, self.filename)
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def dump(self, export_path: str):
        model_path = os.path.join(export_path, self.filename)
        with open(model_path, 'wb') as output:
            pickle.dump(self.model, output)

    def predict(self, vector, top_n=1):
        dt = self.model.pq_model.dtable(query=vector)
        dists = dt.adist(codes=self.model.pq_codes)
        min_n = dists.argsort()[:top_n]
        return min_n

    def fit(self, x):
        np_x = np.asarray(x)
        if (len(np_x)) < self.minimum_required:
            raise RuntimeError("Too less data to train, need at least {0} vectors".format(self.minimum_required))
        pq_model = nanopq.PQ(M=self.m, Ks=min(len(np_x) - 1, self.ks_max))
        pq_model.fit(vecs=np_x, iter=self.n_iter, seed=random.randint(1, 10000))
        self.model = PQModelHolder(pq_model=pq_model,
                                   pq_codes=pq_model.encode(vecs=np_x),
                                   indexed_data=self.indexed_data)

    









