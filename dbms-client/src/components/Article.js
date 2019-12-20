
import React from 'react'
import ReactDOM from 'react-dom'

export default class Article extends React.Component {
    constructor (props) {
        super(props)
        this.state = { visible: true }
    }

    render () {
    return <div className='message-box'>
        Hello {this.props.name}
    </div>
    }
}
