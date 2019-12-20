
import React from 'react'
import ReactDOM from 'react-dom'
import Article from './Article';
import User from './User';
import SearchBar from './Searchbar';


export default class ClientSite extends React.Component {
    constructor (props) {
        super(props)
        this.state = { 
        visible: true,
        SAid: undefined,
        SUid: undefined,
        TypeSearch: undefined
        }  
    }

    callBackSearch = (data) => {
        switch(data.TypeSearch){
            case "article":
                this.setState({
                    SAid: data.SAid,
                    SUid: data.SUid,
                    TypeSearch: data.TypeSearch
                }
                )
                break;
            case "user":
                this.setState({
                    SUid: data.SUid,
                    TypeSearch: data.TypeSearch
                })
                break;
            case "allArticles":
                this.setState({
                    TypeSearch: data.TypeSearch
                })
                break;
            case "allUsers":
                this.setState({
                    TypeSearch: data.TypeSearch
                })
                break;
            default:
                break;
        }
    }

    testConsole(data){
        console.log(data)
    }

    render () {
        let TypeSearch = this.state.TypeSearch;
        if(TypeSearch == "article"){
            return  <div>
                        <SearchBar callBackSearch={this.callBackSearch}/>
                        <Article aid={this.state.SAid} uid={this.state.SUid}></Article>
                        <User></User>
                    </div>
        }
        else if (TypeSearch == "user"){
            return  <div>
                        <SearchBar callBackSearch={this.callBackSearch}/>
                        <Article></Article>
                        <User uid={this.state.SUid}></User>
                    </div>
        }
        else if (TypeSearch == "allArticles"){
            return  <div>
                        <SearchBar callBackSearch={this.callBackSearch}/>
                        <Article></Article>
                        <User></User>
                    </div>
        }
        else if (TypeSearch == "allUsers"){
            return  <div>
                        <SearchBar callBackSearch={this.callBackSearch}/>
                        <Article></Article>
                        <User></User>
                    </div>
        }
        else{
            return  <div>
                        <SearchBar callBackSearch={this.callBackSearch}/>
                        <Article></Article>
                        <User></User>
                    </div>
        }
    }
}
