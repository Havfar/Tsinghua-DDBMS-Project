
import React from 'react'
import ReactDOM from 'react-dom'
import Article from './Article';
import SearchBar from './Searchbar';


export default class ClientSite extends React.Component {
    constructor (props) {
        super(props)
        this.state = { visible: true }  
    }

    render () {
    return <div>
        <SearchBar/>
        <Article></Article>
    </div>
    }
}
