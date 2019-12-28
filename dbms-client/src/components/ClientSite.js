
import React from 'react'
import ReactDOM from 'react-dom'
import Article from './Article';
import User from './User';
import SearchBar from './Searchbar';
import NavBar from './NavBar';
import PopularRank from './PopularRank';


export default class ClientSite extends React.Component {
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
            loggedInUser: "u2d83ecac-c8e3-4340-89fc-745ccc455814",
            fetchedData: undefined,
            url: undefined,
            loadingFinished: undefined,
            users: undefined,
            articles: undefined,
            singleUser: undefined,
            singleArticle: undefined,
        }  
    }

    componentDidMount(){
        switch(this.state.TypeSearch){
            case "allUsers":
                this.genUsers()
                break;
            case "allArticles":
                this.genArticles()
                break;
            case "article":
                this.genArticle()
                break;
            case "user":
                this.genUser()
                break;
            default:
                break;
        }
    }

    componentDidUpdate(){
        switch(this.state.TypeSearch){
            case "allUsers":
                this.genUsers()
                break;
            case "allArticles":
                this.genArticles()
                break;
            case "article":
                this.genArticle()
                break;
            case "user":
                this.genUser()
                break;
            default:
                break;
        }
    }

    genUsers = async() => {
        try {
            let data = await fetch(this.state.url, {
                method: 'GET', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
                cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
                credentials: 'same-origin', // include, *same-origin, omit
                headers: {
                  'Content-Type': 'application/json'
                }
            }).then(response => response.json())

            // this will re render the view with new data
            this.setState({
                TypeSearch: undefined,
              users: data.map((jsonUser, i) => (
                <User fetchReads={this.fetchUserReads} uid={jsonUser.uid} timestamp={jsonUser.timestamp} name={jsonUser.name} gender={jsonUser.gender} email={jsonUser.email} phone={jsonUser.phone} dept={jsonUser.dept} language={jsonUser.language} region={jsonUser.region} role={jsonUser.region} role={jsonUser.role} prefer_tags={jsonUser.prefer_tags} obtained_credits={jsonUser.obtained_credits} age={data.age} compressed={true} collapseTarget={i} id={i}/>
              ))

        })
    }catch (err) {
        console.log(err);
      }
    }

genArticles = async() => {
        try {
            let data = await fetch(this.state.url, {
                method: 'GET', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
                cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
                credentials: 'same-origin', // include, *same-origin, omit
                headers: {
                  'Content-Type': 'application/json'
                }
            }).then(response => response.json())

            // this will re render the view with new data
            this.setState({
                TypeSearch: undefined,
              articles: data.map((jsonArticle, i) => (
                <Article genRead={this.callBackGenRead} aid={jsonArticle.aid} timestamp={jsonArticle.timestamp} title={jsonArticle.title} abstrac={jsonArticle.abstract} article_tags={jsonArticle.article_tags} author={jsonArticle.author} language={jsonArticle.language} text={jsonArticle.text} image={jsonArticle.image} video={jsonArticle.video} category={jsonArticle.category} compressed={true} collapseTarget={i} id={i}/>
              ))
        })
    }catch (err) {
        console.log(err);
      }
}

genUser = async(url) => {
    try {
        let jsonUser = await fetch(this.state.url, {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
              'Content-Type': 'application/json'
            }
        }).then(response => response.json())

        // this will re render the view with new data
        this.setState({
            TypeSearch: undefined,
          singleUser: 
          <User fetchReads={this.fetchUserReads} uid={jsonUser.uid} timestamp={jsonUser.timestamp} name={jsonUser.name} gender={jsonUser.gender} email={jsonUser.email} phone={jsonUser.phone} dept={jsonUser.dept} language={jsonUser.language} region={jsonUser.region} role={jsonUser.region} role={jsonUser.role} prefer_tags={jsonUser.prefer_tags} obtained_credits={jsonUser.obtained_credits} age={jsonUser.age} compressed={false} collapseTarget={1} id={1}/>
        })
}catch (err) {
    console.log(err);
  }
}


genArticle = async(url) => {
    try {
        let jsonArticle = await fetch(this.state.url, {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
              'Content-Type': 'application/json'
            }
        }).then(response => response.json())

        // this will re render the view with new data
        this.setState({
            TypeSearch: undefined,
          singleArticle: 
          <Article genRead={this.callBackGenRead} aid={jsonArticle.aid} timestamp={jsonArticle.timestamp} title={jsonArticle.title} abstrac={jsonArticle.abstract} article_tags={jsonArticle.article_tags} author={jsonArticle.author} language={jsonArticle.language} text={jsonArticle.text} image={jsonArticle.image} video={jsonArticle.video} category={jsonArticle.category} compressed={false} collapseTarget={1} id={1}/>

        })
}catch (err) {
    console.log(err);
  }
}

toggleSearchBar = () =>{
        console.log(this.state.hideSearchBar)
        this.setState({hideSearchBar : !this.state.hideSearchBar})
}

    callBackSearch = async (TypeSearch, searchString, region, category) => {
        let url = ""
        let port = ""
        switch(TypeSearch){
            case "article":
                if(category == 'Technology'){
                        port = '5000'
                }
                else{
                    port = '5001'
                }
                url = 'http://localhost:' + port + '/load_article/?aid=' + searchString + "&uid="+this.state.loggedInUser
                this.setState({
                    SAid: searchString,
                    TypeSearch: TypeSearch,
                    category: category,
                    url: url,
                    searchString: searchString
                }
                )
                break;
            case "user":
                if(region == "Beijing"){
                    port = '5000'
                }
                else{
                    port = '5001'
                }
                url = 'http://localhost:'+port+'/load_user/?uid=' + searchString
                this.setState({
                    SUid: searchString,
                    TypeSearch: TypeSearch,
                    region: region,
                    category: category,
                    url: url,
                    searchString: searchString
                })
                break;
            case "allArticles":
                if(category == 'Technology'){
                    port = '5000'
            }
            else{
                port = '5001'
            }
                url = 'http://localhost:'+port+'/load_all_articles'
                this.setState({
                    TypeSearch: TypeSearch,
                    category: category,
                    region: region,
                    url: url,
                    searchString: searchString
                });
                break;
            case "allUsers":
                if(region == "Beijing"){
                    port = '5000'
                }
                else{
                    port = '5001'
                }
                url = 'http://localhost:'+port+'/load_all_users'

                this.setState({
                    TypeSearch: TypeSearch,
                    region: region,
                    category: category,
                    url: url,
                    searchString: searchString
                })
                break;
            case "readByUser":
                url = 'http://localhost:5000/user_read_table/?uid=' + searchString
                this.setState({
                    TypeSearch: TypeSearch,
                    region: region,
                    category: category,
                    url: url,
                    searchString: searchString
                })
                break;
            case "articleReadByUsers":
                url = 'http://localhost:5000/be_read_by_aid/' + searchString
                this.setState({
                    TypeSearch: TypeSearch,
                    region: region,
                    category: category,
                    url: url,
                    searchString: searchString
                })
            default:
                break;
        }
    }

    pageNumberClicked = (number) => {
        if(number == "next"){
            // No logic to handle going higher than available sites
            this.setState({
                currentPageNumber : this.state.currentPageNumber+1
            }, () => {
                //alert("changed to page:" + number + " now on page:" + this.state.currentPageNumber)
    
            })
        }
        else if(number == "previous"){
            if(this.state.currentPageNumber > 1){

                this.setState({
                    currentPageNumber : this.state.currentPageNumber-1
                }, () => {
                    //alert("changed to page:" + number + " now on page:" + this.state.currentPageNumber)
        
                })
            }
        }
        else{
        this.setState({
            currentPageNumber : number
        }, () => {
            alert("changed to page:" + number + " now on page:" + this.state.currentPageNumber)

        })}
    }
   
    callBackLoggedInUser = (loggedInUser) =>{
        this.setState({
            loggedInUser: loggedInUser
        }, alert("You have logged in as user: " + loggedInUser))
    }

    genClientSite = () => {
        // render site based on TypeSearch

        switch(this.state.TypeSearch){
            case "user":
                return <div>
                    <SearchBar parent={this} callBackSearch={this.callBackSearch}/>
                    {this.state.singleUser}
                </div>
            case "article":
                return <div>
                    <SearchBar parent={this} callBackSearch={this.callBackSearch}/>
                    {this.state.singleArticle}
                </div>
            case "allUsers":
                return <div>
                    <SearchBar parent={this} callBackSearch={this.callBackSearch}/>
                    {this.state.users}
                </div>
            case "allArticles":
                return <div>
                    <SearchBar parent={this} callBackSearch={this.callBackSearch}/>
                    {this.state.articles}
                </div>
                // no TypeSearch eg initial load of site
            default:
                return <div>
                    <SearchBar parent={this} callBackSearch={this.callBackSearch}/>
                        {this.state.singleUser}
                        {this.state.singleArticle}
                        {this.state.users}
                        {this.state.articles}
                </div>
                
        }
    }

    getPopularRank(){
        return(
            <PopularRank genRead={this.callBackGenRead}/>
        )
    }

    getAcitveComponent(){
        switch(this.state.activeComponent){
            case "clientSite":
                return this.genClientSite(this.state.TypeSearch)
            case "PopularRank":
                return this.getPopularRank()
        }
    }

    changeActiveComponent(component){
        this.setState({activeComponent:component})
    }

    callBackGenRead = (aid) => {
        let url = "http://localhost:5000/create_read/?aid=" + aid + "&uid=" + this.state.loggedInUser

        fetch(url, {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
              'Content-Type': 'application/json'
            }
        }).then(response => {console.log(response)}).catch(err => {console.log(err)})

    }

    render () {
        return  <div>
                    <NavBar callBackLoggedInUser={this.callBackLoggedInUser} parent={this}/>
                    <div class="container mt-5">
                            <div class="row">
                                <div class="col-lg-12 text-center"></div>
                                    {this.getAcitveComponent()}
                                    {/* {this.genClientSite(this.state.TypeSearch)} */}
                                    {/* {this.getPopularRank()} */}
                                </div>
                            </div>
                    </div>
    }
}
