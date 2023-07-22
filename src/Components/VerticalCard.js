import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import avatar from '../images/avatar.png'

export default function VerticalCard(props) {

  return (
    <Card sx={{ display: 'flex' }}>
      <CardMedia
        component="img"
        sx={{ width: 151 }}
        image={avatar}
        alt="Live from space album cover"
      />
      <Box sx={{ display: 'flex', flexDirection: 'column' }}>
        <CardContent sx={{ flex: '1 0 auto' }}>
          <Typography component="div" variant="h5">
            Student Name: {props.name}
          </Typography>
          <Typography variant="subtitle1" color="text.secondary" component="div">
            Lab Section: {props.lab}
          </Typography>
          <Typography variant="subtitle1" color="text.secondary" component="div">
            Check in date: {props.date}
          </Typography>
          <Typography variant="subtitle1" color="text.secondary" component="div">
            Other notes: {props.notes}
          </Typography>
        </CardContent>
      </Box>
    </Card>
  );
}