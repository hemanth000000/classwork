// Find and modify a podcast document by its _id, and atomically increment the 'downloads' field by 1
db.podcasts.findAndModify({
  query: {_id: ObjectId("65c45e54c6d23febaede0df0")},// Specify the query to find the document by its _id
  update: {$inc: {downloads: 1}},// Use the $inc operator to increment the 'downloads' field by 1
  new: true,// Return the modified document after the update
});
