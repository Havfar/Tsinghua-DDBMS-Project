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
            topArticles: undefined,
            url: undefined,
            article_id_list: undefined,
            must_load_articles_from_list: undefined,
            shouldLoadArticles: undefined
            }
        }   
    componentDidMount(){
        this.loadArticles()
    }

    changeTemporalGranularity(value){
        this.setState({
            shouldLoadArticles: true,
            temporalGranularity:value
        })
    }

    componentDidUpdate(){
        if(this.state.shouldLoadArticles){
            this.loadArticles()
        }

    }
/*
    getArticlesFromList = async() => {
        let list_of_articles = []
        for (const article_id of this.state.article_id_list){
            try{
            let url = "http://localhost:5000/load_article_from_popular/?aid="+article_id
            let article_object = await fetch(url, {
                method: 'GET', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
                cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
                credentials: 'same-origin', // include, *same-origin, omit
                headers: {
                  'Content-Type': 'application/json'
                }
            }).then(response => response.json());
            list_of_articles.push(article_object)
            }
            catch(err){
                console.log(err)
            }
        }
        this.setState({
            must_load_articles_from_list: false,
        topArticles: list_of_articles.map((jsonArticle, i) => (
            <Article aid={jsonArticle.aid} timestamp={jsonArticle.timestamp} title={jsonArticle.title} abstrac={jsonArticle.abstract} article_tags={jsonArticle.article_tags} author={jsonArticle.author} language={jsonArticle.language} text={jsonArticle.text} image={jsonArticle.image} video={jsonArticle.video} category={jsonArticle.category} compressed={false} collapseTarget={i} id={i}/>
          ))
        })
    }
*/

    getPopularArticlesList = async() => {
        try {
            let url = "http://localhost:5000/popular_rank/?filter=" + this.state.temporalGranularity
            let article_list = await fetch(url, {
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
                shouldLoadArticles: false,
                topArticles: article_list.map((jsonArticle, i) => (
                    <Article genRead={this.props.genRead} aid={jsonArticle.aid} timestamp={jsonArticle.timestamp} title={jsonArticle.title} abstrac={jsonArticle.abstract} article_tags={jsonArticle.article_tags} author={jsonArticle.author} language={jsonArticle.language} text={jsonArticle.text} image={jsonArticle.image} video={jsonArticle.video} category={jsonArticle.category} compressed={false} collapseTarget={i} id={i}/>
                  ))
            })
        }catch (err) {
            console.log(err);
        }
    }

    loadArticles(){
        this.getPopularArticlesList()
    }

    getArticles(){
        return(
            <div className="row mt-5 ">
                <span className="row text-center "><h1 className="col">Most popular article</h1></span>
                {this.state.topArticles}
            </div>
        )
    }


    genPopularArticles = (article_id_list) => {


            // this will re render the view with new data
            this.setState({
                TypeSearch: undefined,
              articles: this.state.article_id_list.map((jsonArticle, i) => (
                <Article genRead={this.props.genRead} aid={jsonArticle.aid} timestamp={jsonArticle.timestamp} title={jsonArticle.title} abstrac={jsonArticle.abstract} article_tags={jsonArticle.article_tags} author={jsonArticle.author} language={jsonArticle.language} text={jsonArticle.text} image={jsonArticle.image} video={jsonArticle.video} category={jsonArticle.category} compressed={true} collapseTarget={i} id={i}/>
              )
    )})
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
