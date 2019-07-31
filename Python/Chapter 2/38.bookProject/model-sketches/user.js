const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const userSchema = new Schema({
  fullname: String,
  username: String,
  password: String,
  wallet: Number,
  ownedBooks: [
    {
      id: book._id,
      currentPage: Number
    }
  ]
});

// newUser = {
//   fullname: "Admin",
//   username: "admin",
//   password: "admin",
//   wallet: 100.0,
//   ownedBooks: []
// };

/*
# bookObject = open("./book_lib/2147-0.txt",
"r")
# for j in range(0,
856):
#     for i in range(0,
25):
#         print(bookObject.readline())
*/
