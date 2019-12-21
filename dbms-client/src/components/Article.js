import React from 'react'

export default class Article extends React.Component {
    constructor(props) {
        super(props)
        this.state = { 
            aid: 6969696969,
            timestamp: "2019-09-09",
            title: "BREAKING NEWS!",
            abstract: "My money's in that office, right? If she start giving me some bullshit about it ain't there, and we got to go someplace else and get it, I'm gonna shoot you in the head then and there. Then I'm gonna shoot that bitch in the kneecaps, find out where my goddamn money is. She gonna tell me too. Hey, look at me when I'm talking to you, motherfucker. You listen: we go in there, and that nigga Winston or anybody else is in there, you the first motherfucker to get shot. You understand?",
            article_tags: "Tags ",
            author: "Alf Prøysen",
            language: "en",
            text: "Well, the way they make shows is, they make one show. That show's called a pilot. Then they show that show to the people who make shows, and on the strength of that one show they decide if they're going to make more shows. Some pilots get picked and become television programs. Some don't, become nothing. She starred in one of the ones that became nothing. Look, just because I don't be givin' no man a foot massage don't make it right for Marsellus to throw Antwone into a glass motherfuckin' house, fuckin' up the way the nigger talks. Motherfucker do that shit to me, he better paralyze my ass, 'cause I'll kill the motherfucker, know what I'm sayin'?",
            image: undefined,
            video: undefined,
            category: "Technology",
            compressed: true
            }
        }   
    componentDidMount(){
        const url = 'http://localhost:5000/load_article/?aid=' + this.props.aid+"&uid="+this.props.uid;
        fetch(url, {
            method: 'GET',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers: {
                'Content-Type':'application/json'
            }
        })
        .then(response => response.json())
        .then(data => this.setState({
            aid: data.aid,
            timestamp: data.timestamp,
            title: data.title,
            abstract: data.abstract,
            article_tags: data.article_tags,
            author: data.author,
            language: data.language,
            text: data.text,
            image: data.image,
            video: data.video,
            category: data.category
        }));
    }

    getCompressedView(){
        return( 
            <div className="card text-left mt-4" onClick={this.toggleCompress}>
                <span className="col-1"/>
                <div className="col">
                    <div className="row">
                        <h2 className="col-10 ml-1 mt-2">{this.state.title}</h2>
                    </div>
                    <div className="row">
                        <p className="col ml-1 font-weight-lighter">{this.state.timestamp}</p>
                    </div>
                    <div className="row">
                        <p className="col">{this.state.text}</p>
                    </div>
                </div>
                <span className="col-1"/>
            </div>
        )
    }

    toggleCompress = () =>{
        this.setState({compressed: !this.state.compressed})
    }

    getFullView(){
        return(
            <div className="card text-left mt-4" onClick={this.toggleCompress}>
                <span className="col-1"/>
                <div className="col">
                    <div className="row mt-3">
                        <img className="col" src="https://tse3-mm.cn.bing.net/th/id/OIP.BFzdEk9ZBP23QuzfF9RYJgHaFj?w=231&h=171&c=7&o=5&dpr=2&pid=1.7"></img>
                    </div>
                    <div className="row">
                        <h2 className="col ml-1 mt-2">{this.state.title}</h2>
                        <p className="col-2 mt-2 font-weight-lighter">{this.state.timestamp}</p>

                    </div>
                    <div className="row">
                        <p className="col ml-1 font-weight-light">by {this.state.author}</p>
                    
                    </div>
                    <div className="row">
                        <p className="col">{this.state.abstract}</p>
                    </div>                    
                    <div className="row">
                        <p className="col">{this.state.text}</p>
                    </div>
                </div>
                <span className="col-1"/>
            </div>
        )
    }
    render (){
            if(this.state.compressed){
                return(
                    this.getCompressedView()
                )
                }
            else{
                return(
                    this.getFullView()
                )
            }
    }
    }
