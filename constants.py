import json

swara_ratio = dict()
swara_ratio["S"] = 1
swara_ratio["R1"] = 256/243.0
swara_ratio["R2"] = 16/15.0
swara_ratio["R3"] = 10/9.0
swara_ratio["G1"] = 32/27.0
swara_ratio["G2"] = 6/5.0
swara_ratio["G3"] = 5/4.0
swara_ratio["M1"] = 4/3.0
swara_ratio["M2"] = 27/20.0
swara_ratio["P"] = 3/2.0
swara_ratio["D1"] = 128/81.0
swara_ratio["D2"] = 8/5.0
swara_ratio["D3"] = 5/3.0
swara_ratio["N1"] = 16/9.0
swara_ratio["N2"] = 9/5.0
swara_ratio["N3"] = 15/8.0
swara_ratio["S2"] = 2


BASE_PATH = "/Users/sudharsantirumalai/Documents/"

PATH_MBID_RAGAID_JSON_PATH = "RagaDataset/Carnatic/_info_/path_mbid_ragaid_formatted.json"

REDUCED = "RagaDataset/Carnatic/_info_/reduced.json"

RAGAID_RAGANAME_JSON_PATH = "RagaDataset/Carnatic/_info_/ragaId_to_ragaName_mapping_formatted.json"

TESTING_FILE_PATH = "RagaDataset/Carnatic/_info_/testing.json"

mbid_to_ragaid = json.load(open(BASE_PATH + PATH_MBID_RAGAID_JSON_PATH))
ragaid_to_raganame = json.load(open(BASE_PATH + RAGAID_RAGANAME_JSON_PATH))


if __name__ == '__main__':
	print(mbid_to_ragaid)
	print(ragaid_to_raganame)
