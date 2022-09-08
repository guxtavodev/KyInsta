import React from 'react';
import ReactDOM from 'react-dom';

class Paragraph extends React.Component {
  render() {
    return(
      <p>{this.props.text}</p>
    )
  }
}

ReactDOM.render( 
  <Paragraph text="Hello" />, 
  document.getElementById('root') 
);
