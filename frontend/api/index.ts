import axios from 'axios';

interface GetCommentResponse {
  content: string
  url: string
}

export const getComment = async (): Promise<GetCommentResponse> => {
  const errorMessage = {
    content: 'Oops, something went wrong, please try again later',
    url: 'Unavailable'
  };
  
  try {
    const res = await axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/comment`);
    if (res.status !== 200) {
      return errorMessage;
    }
    const data = res.data as GetCommentResponse;
    return data
  } catch {
    return errorMessage;
  }
}
