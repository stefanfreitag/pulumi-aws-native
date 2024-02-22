// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sqs

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SQS::Queue
func LookupQueue(ctx *pulumi.Context, args *LookupQueueArgs, opts ...pulumi.InvokeOption) (*LookupQueueResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupQueueResult
	err := ctx.Invoke("aws-native:sqs:getQueue", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupQueueArgs struct {
	// URL of the source queue.
	QueueUrl string `pulumi:"queueUrl"`
}

type LookupQueueResult struct {
	// Amazon Resource Name (ARN) of the queue.
	Arn *string `pulumi:"arn"`
	// For first-in-first-out (FIFO) queues, specifies whether to enable content-based deduplication. During the deduplication interval, Amazon SQS treats messages that are sent with identical content as duplicates and delivers only one copy of the message.
	ContentBasedDeduplication *bool `pulumi:"contentBasedDeduplication"`
	// Specifies whether message deduplication occurs at the message group or queue level. Valid values are messageGroup and queue.
	DeduplicationScope *string `pulumi:"deduplicationScope"`
	// The time in seconds for which the delivery of all messages in the queue is delayed. You can specify an integer value of 0 to 900 (15 minutes). The default value is 0.
	DelaySeconds *int `pulumi:"delaySeconds"`
	// Specifies whether the FIFO queue throughput quota applies to the entire queue or per message group. Valid values are perQueue and perMessageGroupId. The perMessageGroupId value is allowed only when the value for DeduplicationScope is messageGroup.
	FifoThroughputLimit *string `pulumi:"fifoThroughputLimit"`
	// The length of time in seconds for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. The value must be an integer between 60 (1 minute) and 86,400 (24 hours). The default is 300 (5 minutes).
	KmsDataKeyReusePeriodSeconds *int `pulumi:"kmsDataKeyReusePeriodSeconds"`
	// The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK. To use the AWS managed CMK for Amazon SQS, specify the (default) alias alias/aws/sqs.
	KmsMasterKeyId *string `pulumi:"kmsMasterKeyId"`
	// The limit of how many bytes that a message can contain before Amazon SQS rejects it. You can specify an integer value from 1,024 bytes (1 KiB) to 262,144 bytes (256 KiB). The default value is 262,144 (256 KiB).
	MaximumMessageSize *int `pulumi:"maximumMessageSize"`
	// The number of seconds that Amazon SQS retains a message. You can specify an integer value from 60 seconds (1 minute) to 1,209,600 seconds (14 days). The default value is 345,600 seconds (4 days).
	MessageRetentionPeriod *int `pulumi:"messageRetentionPeriod"`
	// URL of the source queue.
	QueueUrl *string `pulumi:"queueUrl"`
	// Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, rather than returning an empty response if a message isn't yet available. You can specify an integer from 1 to 20. Short polling is used as the default or when you specify 0 for this property.
	ReceiveMessageWaitTimeSeconds *int `pulumi:"receiveMessageWaitTimeSeconds"`
	// The string that includes the parameters for the permissions for the dead-letter queue redrive permission and which source queues can specify dead-letter queues as a JSON object.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SQS::Queue` for more information about the expected schema for this property.
	RedriveAllowPolicy interface{} `pulumi:"redriveAllowPolicy"`
	// A string that includes the parameters for the dead-letter queue functionality (redrive policy) of the source queue.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SQS::Queue` for more information about the expected schema for this property.
	RedrivePolicy interface{} `pulumi:"redrivePolicy"`
	// Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (e.g. SSE-KMS or SSE-SQS ).
	SqsManagedSseEnabled *bool `pulumi:"sqsManagedSseEnabled"`
	// The tags that you attach to this queue.
	Tags []aws.Tag `pulumi:"tags"`
	// The length of time during which a message will be unavailable after a message is delivered from the queue. This blocks other components from receiving the same message and gives the initial component time to process and delete the message from the queue. Values must be from 0 to 43,200 seconds (12 hours). If you don't specify a value, AWS CloudFormation uses the default value of 30 seconds.
	VisibilityTimeout *int `pulumi:"visibilityTimeout"`
}

func LookupQueueOutput(ctx *pulumi.Context, args LookupQueueOutputArgs, opts ...pulumi.InvokeOption) LookupQueueResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupQueueResult, error) {
			args := v.(LookupQueueArgs)
			r, err := LookupQueue(ctx, &args, opts...)
			var s LookupQueueResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupQueueResultOutput)
}

type LookupQueueOutputArgs struct {
	// URL of the source queue.
	QueueUrl pulumi.StringInput `pulumi:"queueUrl"`
}

func (LookupQueueOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupQueueArgs)(nil)).Elem()
}

type LookupQueueResultOutput struct{ *pulumi.OutputState }

func (LookupQueueResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupQueueResult)(nil)).Elem()
}

func (o LookupQueueResultOutput) ToLookupQueueResultOutput() LookupQueueResultOutput {
	return o
}

func (o LookupQueueResultOutput) ToLookupQueueResultOutputWithContext(ctx context.Context) LookupQueueResultOutput {
	return o
}

// Amazon Resource Name (ARN) of the queue.
func (o LookupQueueResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// For first-in-first-out (FIFO) queues, specifies whether to enable content-based deduplication. During the deduplication interval, Amazon SQS treats messages that are sent with identical content as duplicates and delivers only one copy of the message.
func (o LookupQueueResultOutput) ContentBasedDeduplication() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *bool { return v.ContentBasedDeduplication }).(pulumi.BoolPtrOutput)
}

// Specifies whether message deduplication occurs at the message group or queue level. Valid values are messageGroup and queue.
func (o LookupQueueResultOutput) DeduplicationScope() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *string { return v.DeduplicationScope }).(pulumi.StringPtrOutput)
}

// The time in seconds for which the delivery of all messages in the queue is delayed. You can specify an integer value of 0 to 900 (15 minutes). The default value is 0.
func (o LookupQueueResultOutput) DelaySeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *int { return v.DelaySeconds }).(pulumi.IntPtrOutput)
}

// Specifies whether the FIFO queue throughput quota applies to the entire queue or per message group. Valid values are perQueue and perMessageGroupId. The perMessageGroupId value is allowed only when the value for DeduplicationScope is messageGroup.
func (o LookupQueueResultOutput) FifoThroughputLimit() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *string { return v.FifoThroughputLimit }).(pulumi.StringPtrOutput)
}

// The length of time in seconds for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. The value must be an integer between 60 (1 minute) and 86,400 (24 hours). The default is 300 (5 minutes).
func (o LookupQueueResultOutput) KmsDataKeyReusePeriodSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *int { return v.KmsDataKeyReusePeriodSeconds }).(pulumi.IntPtrOutput)
}

// The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK. To use the AWS managed CMK for Amazon SQS, specify the (default) alias alias/aws/sqs.
func (o LookupQueueResultOutput) KmsMasterKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *string { return v.KmsMasterKeyId }).(pulumi.StringPtrOutput)
}

// The limit of how many bytes that a message can contain before Amazon SQS rejects it. You can specify an integer value from 1,024 bytes (1 KiB) to 262,144 bytes (256 KiB). The default value is 262,144 (256 KiB).
func (o LookupQueueResultOutput) MaximumMessageSize() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *int { return v.MaximumMessageSize }).(pulumi.IntPtrOutput)
}

// The number of seconds that Amazon SQS retains a message. You can specify an integer value from 60 seconds (1 minute) to 1,209,600 seconds (14 days). The default value is 345,600 seconds (4 days).
func (o LookupQueueResultOutput) MessageRetentionPeriod() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *int { return v.MessageRetentionPeriod }).(pulumi.IntPtrOutput)
}

// URL of the source queue.
func (o LookupQueueResultOutput) QueueUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *string { return v.QueueUrl }).(pulumi.StringPtrOutput)
}

// Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, rather than returning an empty response if a message isn't yet available. You can specify an integer from 1 to 20. Short polling is used as the default or when you specify 0 for this property.
func (o LookupQueueResultOutput) ReceiveMessageWaitTimeSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *int { return v.ReceiveMessageWaitTimeSeconds }).(pulumi.IntPtrOutput)
}

// The string that includes the parameters for the permissions for the dead-letter queue redrive permission and which source queues can specify dead-letter queues as a JSON object.
//
// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SQS::Queue` for more information about the expected schema for this property.
func (o LookupQueueResultOutput) RedriveAllowPolicy() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupQueueResult) interface{} { return v.RedriveAllowPolicy }).(pulumi.AnyOutput)
}

// A string that includes the parameters for the dead-letter queue functionality (redrive policy) of the source queue.
//
// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SQS::Queue` for more information about the expected schema for this property.
func (o LookupQueueResultOutput) RedrivePolicy() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupQueueResult) interface{} { return v.RedrivePolicy }).(pulumi.AnyOutput)
}

// Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (e.g. SSE-KMS or SSE-SQS ).
func (o LookupQueueResultOutput) SqsManagedSseEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *bool { return v.SqsManagedSseEnabled }).(pulumi.BoolPtrOutput)
}

// The tags that you attach to this queue.
func (o LookupQueueResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupQueueResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

// The length of time during which a message will be unavailable after a message is delivered from the queue. This blocks other components from receiving the same message and gives the initial component time to process and delete the message from the queue. Values must be from 0 to 43,200 seconds (12 hours). If you don't specify a value, AWS CloudFormation uses the default value of 30 seconds.
func (o LookupQueueResultOutput) VisibilityTimeout() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupQueueResult) *int { return v.VisibilityTimeout }).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupQueueResultOutput{})
}
