import React from 'react'

export default class NavBar extends React.Component {

    constructor(props) {
    super(props)
    
    this.state = { 
            loggedInUid: undefined
        }
    }  

    logInUser = () =>{
        this.props.callBackLoggedInUser(this.state.loggedInUid)
    }


render(){
    return  <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
                <div class="container">
                    <a class="navbar-brand" href="#">Tsinghua DDBMS</a>
                    <input className="form-control col" type="text" placeholder="Logged in userID" aria-label="Search" value={this.state.search} onChange={e => this.setState({loggedInUid: e.target.value})}/>
                    <button type="button" className="btn btn-primary btn-sm" data-toggle="button" aria-pressed="false" onClick={() =>this.logInUser()}>
                    Log In
                    </button>
                        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarResponsive">
                            <ul class="navbar-nav ml-auto">
                                <li class="nav-item active">
                                    <a class="nav-link" href="#">Home
                                        <span class="sr-only">(current)</span>
                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="#">About</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="#">Services</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="#">Contact</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
        }   
}