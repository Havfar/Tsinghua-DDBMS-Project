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