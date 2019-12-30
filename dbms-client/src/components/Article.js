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
            compressed: true,
            showBeRead: false,
            fetchBeReads: false
            }
        }   
    componentDidMount(){
        this.setState({
                aid: this.props.aid,
                timestamp: this.props.timestamp,
                title: this.props.title,
                abstract: this.props.abstract,
                article_tags: this.props.article_tags,
                author: this.props.author,
                language: this.props.language,
                text: this.props.text,
                image: this.props.image,
                video: this.props.video,
                category: this.props.category,
                compressed: this.props.compressed
            })
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
                        <p className="col">{this.state.abstract}</p>
                    </div>
                </div>
                <span className="col-1"/>
            </div>
        )
    }

    toggleCompress = () =>{
        this.setState({compressed: !this.state.compressed})
    }


    fetchBeReads = async() =>{
        console.log("fetching")

        let url = "http://localhost:5000/be_read_by_aid/?aid="+this.state.aid
        let data = await fetch(url, {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
              'Content-Type': 'application/json'
            }
        }).then(response => response.json()).catch(err => {
            console.log(err)
        })

        // split uid string
        let uidList = data.read_uid_list.split(",")

        this.setState({
            beReadRow: uidList.map((uid, i) => (
                <tr>
                    <th scope="col">{uid}</th>
                </tr>
            )),
            showBeRead: true,
            fetchBeReads: true
        })
    }

    showBeRead = () => {
        if(!this.state.showBeRead){
            return(
                <button className="btn btn-lg btn-light" onClick={this.fetchBeReads}> Get article user reads </button>
                )
        }
        else if(!this.state.fetchBeReads && this.state.showBeRead){
            console.log("YAY")
            return (
                <table class="table mt-5">
                    <thead>
                        <tr>
                            <th scope="col">uid</th>
                        </tr>
                    </thead>
                    <tr>
                        No bereads available
                    </tr>
                </table>
            )
        }
        else{
            return (
                <table class="table mt-5">
                <thead>
                    <tr>
                        <th scope="col">uid</th>
                    </tr>
                </thead>
                {this.state.readRows}
            </table>
        )
        }

    }


    getFullView(){
        this.props.genRead(this.state.aid)
        return(
            <div className="card text-left " onClick={this.toggleCompress}>
                <span className="col-1"/>
                <div className="col">
                    <div className="row mt-3">
                        <img className="col" src={"data:image/jpg;base64," + this.state.image}></img>
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
                    {this.showBeRead()}
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
