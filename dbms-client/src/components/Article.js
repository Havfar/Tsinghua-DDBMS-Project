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
    category: undefined
    }
}   


componentDidMount(){

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

    // display the user in a div
    render () {
    return <div>
        <h1>{this.state.title}</h1>
        <div>{this.state.aid}</div>
        <div>{this.state.timestamp}</div>
        <div>{this.state.abstract}</div>
        <div>{this.state.article_tags}</div>
        <div>{this.state.author}</div>
        <div>{this.state.language}</div>
        <div>{this.state.text}</div>
        <div>{this.state.image}</div>
        <div>{this.state.video}</div>
        <div>{this.state.category}</div>
    </div>
  }
}
