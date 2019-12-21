
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
            TypeSearch: "user",
            hideSearchBar: false,
            toDoList: ["per", "paal", "askeladden"],
            currentPageNumber : 1
        }  
    }

    toggleSearchBar = () =>{
        console.log(this.state.hideSearchBar)
        this.setState({hideSearchBar : !this.state.hideSearchBar})
    }

    callBackSearch = (TypeSearch, searchString, region, category) => {
        switch(TypeSearch){
            case "article":
                this.setState({
                    SAid: searchString,
                    TypeSearch: TypeSearch,
                    category: category
                }
                )
                break;
            case "user":
                this.setState({
                    SUid: searchString,
                    TypeSearch: TypeSearch,
                    region: region
                })
                break;
            case "allArticles":
                this.setState({
                    TypeSearch: TypeSearch,
                    category: category
                })
                break;
            case "allUsers":
                this.setState({
                    TypeSearch: TypeSearch,
                    region: region
                })
                break;
            default:
                break;
        }
    }


    testConsole(search){
        console.log(search)
    }

    pageNumberClicked = (number) => {
        if(number == "next"){
            // No logic to handle going higher than available sites
            this.setState({
                currentPageNumber : this.state.currentPageNumber+1
            }, () => {
                alert("changed to page:" + number + " now on page:" + this.state.currentPageNumber)
    
            })
        }
        else if(number == "previous"){
            if(this.state.currentPageNumber > 1){

                this.setState({
                    currentPageNumber : this.state.currentPageNumber-1
                }, () => {
                    alert("changed to page:" + number + " now on page:" + this.state.currentPageNumber)
        
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

    genArticles = (someList) => {
        let counter = 0;
        const items = someList.map((item) => {
            counter += 1;
            return <li>
                {counter}
                <Article compressed={true} collapseTarget={counter} id={counter}/>
            </li>}
            )
            counter += 1;
            return items
    }

    genUsers = (someList) => {
        let counter = 0;
        const items = someList.map((item) => {
            counter += 1;
            return <li>
                {counter}
                <User compressed={true} item={item} collapseTarget={counter} id={counter}/>
            </li>}
            )
            counter += 1;
            return items
    }

    render () {
        let TypeSearch = this.state.TypeSearch;
        if(TypeSearch == "article"){
            return  <div>
                        <SearchBar parent={this} hide={this.state.hideSearchBar} callBackSearch={this.callBackSearch}/>
                        <Article aid={this.state.SAid} uid={this.state.SUid} compressed={false}></Article>
                        <User articleMode={true}></User>
                    </div>
        }
        else if (TypeSearch == "user"){
            return  <div>
                        <SearchBar parent={this}callBackSearch={this.callBackSearch}/>
                        <User uid={this.state.SUid}></User>
                    </div>
        }
        else if (TypeSearch == "allArticles"){
            const items = this.genArticles(this.state.toDoList)
            return  <div>
                <p>{this.state.TypeSearch}</p>
                        <SearchBar parent={this} callBackSearch={this.callBackSearch}/>
                        <div>{items}</div>
                        <nav aria-label="Page navigation example">
                            <ul class="pagination">
                                <li class="page-item">
                                    <a class="page-link" href="#" aria-label="Previous" onClick={ () => this.pageNumberClicked("previous")}>
                                        <span aria-hidden="true">&laquo;</span>
                                    </a>
                                </li>
                                    <li class="page-item"><a class="page-link" href="#" onClick={ () => this.pageNumberClicked(1)}>1</a></li>
                                    <li class="page-item"><a class="page-link" href="#" onClick={ () => this.pageNumberClicked(2)}>2</a></li>
                                    <li class="page-item"><a class="page-link" href="#" onClick={ () => this.pageNumberClicked(3)}>3</a></li>
                                <li class="page-item">
                                    <a class="page-link" href="#" aria-label="Next" onClick={ () => this.pageNumberClicked("next")}>
                                    <   span aria-hidden="true">&raquo;</span>
                                    </a>
                                </li>
                            </ul>
                        </nav>
                        <User articleMode={true}/>
                    </div>
        }
        else if (TypeSearch == "allUsers"){
            const items = this.genUsers(this.state.toDoList)

            return  <div>
                        <p>{this.state.TypeSearch}</p>
                        <SearchBar parent={this} callBackSearch={this.callBackSearch}/>
                        <div>{items}</div>

                        <nav aria-label="Page navigation example">
                            <ul class="pagination">
                                <li class="page-item">
                                    <a class="page-link" href="#" aria-label="Previous" onClick={ () => this.pageNumberClicked("previous")}>
                                        <span aria-hidden="true">&laquo;</span>
                                    </a>
                                </li>
                                    <li class="page-item"><a class="page-link" href="#" onClick={ () => this.pageNumberClicked(1)}>1</a></li>
                                    <li class="page-item"><a class="page-link" href="#" onClick={ () => this.pageNumberClicked(2)}>2</a></li>
                                    <li class="page-item"><a class="page-link" href="#" onClick={ () => this.pageNumberClicked(3)}>3</a></li>
                                <li class="page-item">
                                    <a class="page-link" href="#" aria-label="Next" onClick={ () => this.pageNumberClicked("next")}>
                                    <   span aria-hidden="true">&raquo;</span>
                                    </a>
                                </li>
                            </ul>
                        </nav>
                    </div>
        }
        else{
            return  <div>
                        <SearchBar parent={this} callBackSearch={this.callBackSearch}/>
                        <User/>
                    </div>
        }
    }
}
