
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
            parent: props.parent
        };
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
                <label className="radio-inline col"><input type="radio" name="optradio" checked={this.state.category==="Technology"} onChange={this.changeCategory} value="Beijing"/> &nbsp;Technology</label>
                <span className="col"/>
                <label className="radio-inline col"><input type="radio" name="optradio" checked={this.state.category==="Science"} onChange={this.changeCategory} value="Hong Kong"/>&nbsp; Science </label>
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

    getFilters(){

    }

    search(){
        if(this.state.searchCategory === "Users"){
            this.state.parent.testConsole("users " + this.state.search.toString()+  ", " +this.state.region.toString())
        }else if(this.state.searchCategory === "Articles"){
            this.state.parent.testConsole("Articles " + this.state.search + ", " + this.state.category)
        }
    }

    render(){
        return(
            <div className="md-form mt-0">
                <div className="row">
                    {this.getCategorySelection()}
                    <input className="form-control col" type="text" placeholder="Search" aria-label="Search" value={this.state.search} onChange={e => this.setState({search: e.target.value})}/>
                    <button type="button" className="btn btn-primary col-1 ml-1" data-toggle="button" aria-pressed="false" onClick={() =>this.search()}>
                        Search
                    </button>
                </div>
                {this.getSearchOptions()}
            </div>
        )
    }
}
