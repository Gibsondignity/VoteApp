import React,{useState}from 'react'
import { useRouter } from "next/router";

const categories = ({NominesData}) => {
    const router = useRouter();
  const { categoryid } = router.query;

  return (
    <div>{categoryid}</div>
  )
}

export default categories;



export async function getServerSideProps(ctx) {
  // console.log(ctx.query.categoryid)
  const nomines = await fetch("http://localhost:8000/api/nominees%22")
  const  nominesData= await nomines.json();
  // console.log(nominesData)


// let Data = nominesData.filter(nominee => nominee.category == ctx.query.categoryid)
// console.log(Data)
for (let i = 0; i < nominesData.length; i++) {

  console.log(nominesData[i].category == ctx.query.categoryid)
}
// console.log(nominesData[3].category  == ctx.query.categoryid)

    return {
      props: {
        NominesData: nominesData
      }

  }


 
}