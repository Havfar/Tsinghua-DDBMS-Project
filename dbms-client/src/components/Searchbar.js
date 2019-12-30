
import React from 'react'
import ReactDOM from 'react-dom'

export default class SearchBar extends React.Component  {
    constructor (props) {
        super(props);
        this.state = { 
            searchCategory: "",
            alternatives: ["Users", "Articles"],
            region: "Beijing",
            category: "Technology",
            search: "",
            parent: props.parent,
        };
        console.log(props)
    }

    changeSearch = (e) => {this.setState({search : e.target.value})}
    changeSearchCategory = (e) => {this.setState({searchCategory : e.target.value})}
    changeRegion = (e) => {this.setState({region: e.target.value})}
    changeCategory = (e) => {this.setState({category: e.target.value})}

    getCategorySelection(){
        return(
            <select className="custom-select mr-1 col-2" onChange={this.changeSearchCategory}>
                <option value={null}> - </option>
                    {this.state.alternatives.map(function(item) {
                    return <option value={item}>{item}</option>
                })}
            </select>)
    }

    getRegions(){
        return(
            <div className="row mt-3">
                <span className="col"/>
                <label className="radio-inline col"><input type="radio" name="optradio" checked={this.state.region==="Beijing"} onChange={this.changeRegion} value="Beijing"/> &nbsp;Beijing</label>
                <span className="col"/>
                <label className="radio-inline col"><input type="radio" name="optradio" checked={this.state.region==="Hong Kong"} onChange={this.changeRegion} value="Hong Kong"/>&nbsp; Hong Kong</label>
                <span className="col"/>
            </div>
        )
    }

    getCategories(){
        return(
            <div className="row mt-3">
                <span className="col"/>
                <label className="radio-inline col"><input type="radio" name="optradio" checked={this.state.category==="Technology"} onChange={this.changeCategory} value="Technology"/> &nbsp;Technology</label>
                <span className="col"/>
                <label className="radio-inline col"><input type="radio" name="optradio" checked={this.state.category==="Science"} onChange={this.changeCategory} value="Science"/>&nbsp; Science </label>
                <span className="col"/>
            </div>
        )
    }

    getSearchOptions(){
        if(this.state.searchCategory === "Users"){
            return this.getRegions()
        }else if(this.state.searchCategory === "Articles"){
            return this.getCategories()
        }else{
            return
        }
    }

    search(){
        let TypeSearch = ""
        let searchString = ""
        if(this.state.searchCategory === "Users"){
            if(this.state.search === ""){
                TypeSearch = "allUsers"
            }else{
                TypeSearch = "user"

            }
        }else if(this.state.searchCategory === "Articles"){
            if(this.state.search === ""){
                TypeSearch = "allArticles"

            }else{
                TypeSearch = "article"
            }
        }
        this.state.parent.callBackSearch(TypeSearch, this.state.search, this.state.region, this.state.category)
    }

    getComponentClassName(){
        if(this.state.parent.state.hideSearchBar){
            return "md-form mt-0 d-none"
        }else{
            return "md-form mt-0"
        }

    }

    render(){

        return(
            <div className={this.getComponentClassName()} >
                <div className="row">
                    {this.getCategorySelection()}
                    <input className="form-control col" type="text" placeholder="Search" aria-label="Search" onChange={e => this.setState({search: e.target.value})}/>
                    <button type="button" className="btn btn-primary col-1 ml-1" data-toggle="button" aria-pressed="false" onClick={() =>this.search()}>
                        Search
                    </button>
                </div>
                {this.getSearchOptions()}
            </div>
        )
    }
}
