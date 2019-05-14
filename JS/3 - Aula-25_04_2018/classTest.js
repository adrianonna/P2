class Post {
    get title() {
      return this._title
    }
    set title(title) {
      this._title = title
    }
  }
  var post = new Post()
  
  console.log(post)       //=> Post {}
  
  // set
  post.title = 'lorem ipsum dolor'
  
  console.log(post)       //=> Post { _title: 'lorem ipsum dolor' }
  console.log(post.title) //=> 'lorem ipsum dolor' / get