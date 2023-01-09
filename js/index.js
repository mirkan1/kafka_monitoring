const { Kafka } = require('kafkajs')

const kafka = new Kafka({
  clientId: 'quickstart-events',
  brokers: ['localhost:9092']
})

const producer = kafka.producer()
const consumer = kafka.consumer({ groupId: 'quickstart-events' })

const run = async () => {
  // Producing
  await producer.connect()
  producer.logger().info('Connected to Kafka')
  await producer.send({
    topic: 'quickstart-events-1',
    messages: [
      { value: 'Hello KafkaJS user!' },
    ],
  })

  // Consuming
//   await consumer.connect()
//   await consumer.subscribe({ topic: 'quickstart-events', fromBeginning: true })

//   await consumer.run({
//     eachMessage: async ({ topic, partition, message }) => {
//       console.log({
//         partition,
//         offset: message.offset,
//         value: message.value.toString(),
//       })
//     },
//   })
}

run().catch(console.error)