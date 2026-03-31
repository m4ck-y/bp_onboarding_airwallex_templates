/* 30 - MARZO - 2026 */
profile_doc = {
    profile: "COMERCIALIZADORA TOPIK SA DE CV",
    max_txn_per_day: 10,
    max_amount_per_day: 10000, // outbound transactions daily
    min_time_between_txn: 1,
    currency: ["CAD", "USD", "EUR", "MXN", "GBP"],
    specified_income: 16667, // outbound transactions monthly
    max_score_kyt: 30,
    max_txn_same_amount: 5,
    max_txn_consecutive: 5,
    max_consecutive_amount: 5,
    min_consecutive_amount: 10,
    max_days_inactive: 90,
    max_amount_per_txn: 7000, // outbound transactions per transaction
    created_at: new Date(),
    updated_at: new Date()
};
result_transfer_rules = db.TransferRules.insertOne(profile_doc);

inserted_id_str = result_transfer_rules.insertedId.toString();

db.UsersProfileRules.insertOne({
    user_id: 378,
    username: "JESUS GOMEZ MARTINEZ", // sumsub benerificiary[director, representative]
    email: "serviciosadmonycontrol@grupontemx.com", // sumsub company email
    profile_id: inserted_id_str,
    company_id: 334
});





/* 30 - MARZO - 2026 */
/* BEATNORTH LLC */
db.UserProfiles.insertOne({
    "IdUserBanpay": 378,
    "UserNickname": "",
    "UserPin": "",
    "UserAvatar": "",
    "FavoriteCurrency": "CAD",
    "FavoriteTimezone": "America/Vancouver (PDT)"
});