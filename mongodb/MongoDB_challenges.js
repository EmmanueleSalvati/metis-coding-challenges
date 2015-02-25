db = db.getSiblingDB('dsbc');
// print(db.getCollectionNames());

printjson(db.hmm.aggregate([{
    $project: {
        _id: 0,
        'cast': true
    }
}, {
    $unwind: "$cast"
}, {
    $group: {
        _id: "$cast",
        count: {
            $sum: 1
        }
    }
}, {
    $sort: {
        count: -1
    }
}]));

// db.hmm.aggregate([{
//     $project: {
//         _id: 0,
//         'cast': true
//     }
// }, {
//     $unwind: "$cast"
// }, {
//     $group: {
//         _id: "$cast",
//         count: {
//             $sum: 1
//         }
//     }
// }, {
//     $sort: {
//         count: -1
//     }
// }, {
//     $out: "bycast"
// }]);

// db.bycast.find();
