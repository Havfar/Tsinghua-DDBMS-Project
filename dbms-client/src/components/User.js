import React from 'react'

export default class User extends React.Component {

constructor(props) {
  super(props)
  
  this.state = { 
    uid: undefined,
    timestamp: undefined,
    name: undefined,
    gender: undefined,
    email: undefined,
    phone: undefined,
    dept: undefined,
    language: undefined,
    role: undefined,
    prefer_tags: undefined,
    obtained_credits: undefined
    }
}   

componentDidMount(){

    const url = 'http://localhost:5000/load_user/?uid=' + this.props.uid;
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
        uid: data.uid,
        timestamp: data.timestamp,
        name: data.name,
        gender: data.gender,
        email: data.email,
        phone: data.phone,
        dept: data.dept,
        language: data.language,
        role: data.role,
        prefer_tags: data.prefer_tags,
        obtained_credits: data.obtained_credits
    }));
}
    // display the user in a div
    render () {
    return <div>

<div class="card" style={{width: "100%"}}>
    <ul class="list-group list-group-flush">
    <li class="list-group-item"><h1>Name{this.state.name}</h1></li>
    <li class="list-group-item"><div>role{this.state.role}</div></li>
    <li class="list-group-item"><div>dept{this.state.dept}</div></li>
    <li class="list-group-item"><h6 class="card-subtitle mb-2 text-muted">email{this.state.email}</h6></li>
    <li class="list-group-item"><h6 class="card-subtitle mb-2 text-muted">phone{this.state.phone}</h6></li>
    <li class="list-group-item">
    <p>
  <button class="btn btn-primary btn-sm" type="button" data-toggle="collapse" data-target="#user" aria-expanded="false" aria-controls="collapseExample">
    <h5>extra information</h5>
  </button>
</p>
<div class="collapse" id="user">
  <div class="card card-body">
  <ul class="list-group list-group-flush">
    <li class="list-group-item">gender{this.state.gender}</li>
    <li class="list-group-item">language{this.state.language}</li>
    <li class="list-group-item">prefer_tags{this.state.prefer_tags}</li>
    <li class="list-group-item">obtained_credits{this.state.obtained_credits}</li>
    <li class="list-group-item">timestamp{this.state.timestamp}</li>
    <li class="list-group-item"><a href="#" class="badge badge-info">uid{this.state.id}</a></li>
  </ul>
  </div>
</div>
    </li>
  </ul>
</div>

        <h1>{this.state.name}</h1>
        <div>{this.state.uid}</div>
        <div>{this.state.timestamp}</div>
        <div>{this.state.gender}</div>
        <div>{this.state.email}</div>
        <div>{this.state.phone}</div>
        <div>{this.state.dept}</div>
        <div>{this.state.language}</div>
        <div>{this.state.role}</div>
        <div>{this.state.prefer_tags}</div>
        <div>{this.state.obtained_credits}</div>
    </div>
  }
}