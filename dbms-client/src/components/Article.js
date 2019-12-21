import React from 'react'

export default class Article extends React.Component {

constructor(props) {
  super(props)

    // kjøre funksjon for å laste inn userdata

  this.state = { 
    aid: undefined,
    timestamp: undefined,
    title: undefined,
    abstract: undefined,
    article_tags: undefined,
    author: undefined,
    language: undefined,
    text: undefined,
    image: undefined,
    video: undefined,
    category: undefined,
    compressed: undefined
    }
}   


componentDidMount(){

  // Is it compressed?
  this.setState({
    compressed: this.props.compressed
  })

    const url = 'http://localhost:5000/load_article/?aid=' + this.props.aid+"&uid="+this.props.uid;
    fetch(url, {
        method: 'GET',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type':'application/json'
        }
    })
    .then(response => response.json())
    .then(data => this.setState({
        aid: data.aid,
        timestamp: data.timestamp,
        title: data.title,
        abstract: data.abstract,
        article_tags: data.article_tags,
        author: data.author,
        language: data.language,
        text: data.text,
        image: data.image,
        video: data.video,
        category: data.category
    }));
}

    render () {
      if(!this.state.compressed){
    return <div>
        <div class="card" style={{width: "100%"}}>
    <ul class="list-group list-group-flush">
    <li class="list-group-item"><h1>Tittel{this.state.title}</h1></li>
    <li class="list-group-item"><h6 class="card-subtitle mb-2 text-muted">abstract{this.state.abstract}</h6></li>
    <li class="list-group-item"><img src="..." class="card-img-top" alt="..."/></li>
    <li class="list-group-item"><div>en lang tekst som er en artikkel{this.state.text}</div></li>
    <li class="list-group-item">
    <p>
  <button class="btn btn-primary btn-sm" type="button" data-toggle="collapse" data-target="#exampleCollapse" aria-expanded="false" aria-controls="collapseExample">
    <h5>extra information</h5>
  </button>
</p>
<div class="collapse" id="exampleCollapse">
  <div class="card card-body">
  <ul class="list-group list-group-flush">
    <li class="list-group-item">author{this.state.author}</li>
    <li class="list-group-item">language{this.state.language}</li>
    <li class="list-group-item">category{this.state.category}</li>
    <li class="list-group-item">VIDEO{this.state.video}</li>
    <li class="list-group-item">timestamp{this.state.timestamp}</li>
    <li class="list-group-item">aid{this.state.aid}</li>
    <li class="list-group-item"><a href="#" class="badge badge-primary">article_tags{this.state.article_tags}</a></li>
  </ul>
  </div>
</div>
    </li>
  </ul>
</div>
{/*
        <h1>Tittel{this.state.title}</h1>
        <div>aid{this.state.aid}</div>
        <div>timestamp{this.state.timestamp}</div>
        <div>abstract{this.state.abstract}</div>
        <div>article_tags{this.state.article_tags}</div>
        <div>author{this.state.author}</div>
        <div>language{this.state.language}</div>
        <div>en lang tekst som er en artikkel{this.state.text}</div>
        <div>BILDE{this.state.image}</div>
        <div>VIDEO{this.state.video}</div>
<div>category{this.state.category}</div>*/}
    </div>}
    else{
      return <div>
      <div class="card" style={{width: "100%"}}>
  <ul class="list-group list-group-flush">
  <li class="list-group-item">
<button class="btn btn-primary btn-sm" style={{width: "100%"}} type="button" data-toggle="collapse" data-target={"#collapseExample"+this.props.id} aria-expanded="false" aria-controls="collapseExample">
<h1>Tittel{this.state.title}</h1>
</button>
<div class="collapse" id={"collapseExample"+this.props.id}>
<div class="card card-body">
  <li class="list-group-item"><h6 class="card-subtitle mb-2 text-muted">abstract{this.state.abstract}</h6></li>
  <li class="list-group-item"><img src="..." class="card-img-top" alt="..."/></li>
  <li class="list-group-item"><div>en lang tekst som er en artikkel{this.state.text}</div></li>
  <li class="list-group-item">author{this.state.author}</li>
  <li class="list-group-item">language{this.state.language}</li>
  <li class="list-group-item">category{this.state.category}</li>
  <li class="list-group-item">VIDEO{this.state.video}</li>
  <li class="list-group-item">timestamp{this.state.timestamp}</li>
  <li class="list-group-item">aid{this.state.aid}</li>
  <li class="list-group-item"><a href="#" class="badge badge-primary">article_tags{this.state.article_tags}</a></li>
</div>
</div>
  </li>
</ul>
</div>
</div>
    }
  }
}
