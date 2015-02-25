db = db.getSiblingDB('dsbc');

## Challenge 2

db.hmm.aggregate([{$project: {_id: 0, 'cast': true}}, {$unwind: "$cast"},
    {$group: {_id: "$cast", count: {$sum: 1}}},
    {$sort: {count: -1}}]));

Optional: I can add $out in the pipeline
{$out: "bycast"}
db.bycast.find();

## Challenge 4, well... this is only a part, rest in pymongo
hmm.aggregate([{$project: {_id: 0, 'metal_cred': 1}}, {$unwind: '$metal_cred'}, {$match: {metal_cred: {$ne: "METAL CRED"}}}])

