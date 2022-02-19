import React from "react";
import { Card, Button } from "react-bootstrap";

function VotingCard(props) {
  let { team, incrementVoteCount } = props;

  return (
    <Card style={{ width: "18rem" }}>
      {/* <Card.Img variant="top" src={`/assets/images/${team.logo}`} /> */}
      <Card.Body>
        <Card.Title>{}</Card.Title>
        <Button variant="success" onClick={() => incrementVoteCount(team._id)}>
          Vote
        </Button>
      </Card.Body>
    </Card>
  );
}
export default VotingCard;