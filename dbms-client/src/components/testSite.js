
import React from 'react'
import ReactDOM from 'react-dom'
import Article from './Article';
import User from './User';
import SearchBar from './Searchbar';
import NavBar from './NavBar';
import PopularRank from './PopularRank';


export default class TestSite extends React.Component {
    constructor (props) {
        super(props)
        this.state = { 
            visible: true,
            SAid: undefined,
            SUid: undefined,
            TypeSearch: undefined,
            hideSearchBar: false,
            toDoList: ["per", "paal", "askeladden"],
            currentPageNumber : 1,
            activeComponent:'clientSite',
            loggedInUser: undefined,
            fetchedData: undefined,
            url: undefined,
            loadingFinished: undefined,
            users: undefined,
            articles: undefined,
            singleUser: undefined,
            singleArticle: undefined,
        }  
    }



toggleSearchBar = () =>{
        console.log(this.state.hideSearchBar)
        this.setState({hideSearchBar : !this.state.hideSearchBar})
}


    render () {
        return  <div>
                    <NavBar callBackLoggedInUser={this.callBackLoggedInUser} parent={this}/>
                    <div class="container mt-5">
                            <div class="row">
                                <User/>
                                </div>
                            </div>
                    </div>
    }
}
