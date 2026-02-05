from Bio import SeqFeature

# 명확한 position
start_pos=SeqFeature.ExactPosition(15)
end_pos=SeqFeature.ExactPosition(30)
location=SeqFeature.FeatureLocation(start_pos, end_pos)
print(start_pos,end_pos,location)

# 명확하지 않은 position
start_pos2 = SeqFeature.AfterPosition(1)
end_pos2 = SeqFeature.BeforePosition(8)
# end_pos2 = SeqFeature.BetweenPosition(9, left=8, right=9)
my_location = SeqFeature.FeatureLocation(start_pos2, end_pos2)
print(start_pos2,end_pos2,my_location)