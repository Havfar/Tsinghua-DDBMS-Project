import React from 'react'

export default class NavBar extends React.Component {

    constructor(props) {
    super(props)
    
    this.state = { 
            loggedInUid: "u2d83ecac-c8e3-4340-89fc-745ccc455814",
            parent:props.parent,
            active:'clientSite'

        }
    }  

    logInUser = () =>{
        this.props.callBackLoggedInUser(this.state.loggedInUid)
    }

    changeActiveComponent(component){
        this.setState({active:component})
        this.state.parent.changeActiveComponent(component)
    }
    
    getClassName(string){
        if(this.state.active === string){
            return "nav-item active"
        }else{
            return "nav-item "
        }
    }


render(){
    return  <nav className="navbar navbar-expand-lg navbar-dark bg-dark static-top">
                <div className="container">
                    <a className="navbar-brand" href="#">Tsinghua DDBMS</a>
                        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                            <span className="navbar-toggler-icon"></span>
                        </button>
                        <div className="collapse navbar-collapse" id="navbarResponsive">
                            <ul className="navbar-nav ml-auto">
                                <li>
                                <span className="row col"><input className="form-control sm col-8" type="text" placeholder="Logged in userID" aria-label="Search" value={this.state.loggedInUid} onChange={e => this.setState({loggedInUid: e.target.value})}/>
                                <button type="button" className="btn btn-primary btn-md col-4" data-toggle="button" aria-pressed="false" onClick={() =>this.logInUser()}> Log In </button>
                                </span>
                                </li>
                                <li className={this.getClassName("clientSite")}>
                                    <a className="nav-link" href="#" onClick={() => this.changeActiveComponent('clientSite')}>Home
                                        <span className="sr-only">(current)</span>
                                    </a>
                                </li>
                                <li className={this.getClassName("PopularRank")}>
                                    <a className="nav-link" href="#" onClick={() => this.changeActiveComponent('PopularRank')}>Popular rank</a>
                                </li>
                                <li className={this.getClassName()}>
                                    <a className="nav-link" href="#">Services</a>
                                </li>   
                            </ul>
                        </div>
                    </div>
                </nav>
        }   
}