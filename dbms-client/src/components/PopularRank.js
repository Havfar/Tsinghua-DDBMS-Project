import React from 'react'
import Article from './Article';
import { element } from 'prop-types';


export default class PopularRank extends React.Component {
    constructor(props) {
        super(props)
        this.state = { 
            pid: 6969696969,
            timestamp: "2019-09-09",
            temporalGranularity: "daily",
            aidList: [],
            category: "",
            topArticles: [1,2,3,4,5],
            }
        }   
    componentDidMount(){
        this.loadArticles()
    }

    changeTemporalGranularity(value){
        this.loadArticles()
        this.setState({temporalGranularity:value})
    }

    loadArticles(){

    }

    getArticles(){
        return(
            <div className="row mt-5 ">
                <span className="row text-center "><h1 className="col">Most popular article</h1></span>
                {this.state.topArticles.map(function(item) {
                    return <Article/>
                })}
            </div>
        )
    }

    getActiveButton(value){
        if(this.state.temporalGranularity === value){
            return "btn btn-primary "
        }else{
            return "btn btn-outline-primary"
        }
    }

    render (){
        return(
            <div className="row mt-3" style={{justifyContent:"center"}}>
                <div class="btn-group col  " role="group" aria-label="Basic example">
                    <button type="button" value="daily" className={this.getActiveButton("daily")} onClick={() => this.changeTemporalGranularity("daily")}>Daily</button>
                    <button type="button" value="weekly" className={this.getActiveButton("weekly")} onClick={() => this.changeTemporalGranularity("weekly")}>Weekly</button>
                    <button type="button" value="mothly" className={this.getActiveButton("monthly")} onClick={() => this.changeTemporalGranularity("monthly")}>Mothly</button>
                </div>
                {this.getArticles()}
            </div>
        )
    }
    }
