from Bio import SeqIO
record=SeqIO.read("/home/koreanraichu/Octodon degus insulin.gb",'genbank')
for feature in record.features:
    # print(feature.type)
    # Feature의 type에 대해 서술하는 영역
    # print(feature.location)
    # Feature의 위치에 대해 서술하는 영역
    print(feature.qualifiers)
    # Feature를 딕셔너리 형태로 저장했단다