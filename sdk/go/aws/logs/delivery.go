// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package logs

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This structure contains information about one delivery in your account.
//
// A delivery is a connection between a logical delivery source and a logical delivery destination.
//
// For more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).
type Delivery struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) that uniquely identifies this delivery.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The ARN of the delivery destination that is associated with this delivery.
	DeliveryDestinationArn pulumi.StringOutput `pulumi:"deliveryDestinationArn"`
	// Displays whether the delivery destination associated with this delivery is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.
	DeliveryDestinationType pulumi.StringOutput `pulumi:"deliveryDestinationType"`
	// The unique ID that identifies this delivery in your account.
	DeliveryId pulumi.StringOutput `pulumi:"deliveryId"`
	// The name of the delivery source that is associated with this delivery.
	DeliverySourceName pulumi.StringOutput `pulumi:"deliverySourceName"`
	// The tags that have been assigned to this delivery.
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewDelivery registers a new resource with the given unique name, arguments, and options.
func NewDelivery(ctx *pulumi.Context,
	name string, args *DeliveryArgs, opts ...pulumi.ResourceOption) (*Delivery, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DeliveryDestinationArn == nil {
		return nil, errors.New("invalid value for required argument 'DeliveryDestinationArn'")
	}
	if args.DeliverySourceName == nil {
		return nil, errors.New("invalid value for required argument 'DeliverySourceName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"deliveryDestinationArn",
		"deliverySourceName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Delivery
	err := ctx.RegisterResource("aws-native:logs:Delivery", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDelivery gets an existing Delivery resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDelivery(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeliveryState, opts ...pulumi.ResourceOption) (*Delivery, error) {
	var resource Delivery
	err := ctx.ReadResource("aws-native:logs:Delivery", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Delivery resources.
type deliveryState struct {
}

type DeliveryState struct {
}

func (DeliveryState) ElementType() reflect.Type {
	return reflect.TypeOf((*deliveryState)(nil)).Elem()
}

type deliveryArgs struct {
	// The ARN of the delivery destination that is associated with this delivery.
	DeliveryDestinationArn string `pulumi:"deliveryDestinationArn"`
	// The name of the delivery source that is associated with this delivery.
	DeliverySourceName string `pulumi:"deliverySourceName"`
	// The tags that have been assigned to this delivery.
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a Delivery resource.
type DeliveryArgs struct {
	// The ARN of the delivery destination that is associated with this delivery.
	DeliveryDestinationArn pulumi.StringInput
	// The name of the delivery source that is associated with this delivery.
	DeliverySourceName pulumi.StringInput
	// The tags that have been assigned to this delivery.
	Tags aws.TagArrayInput
}

func (DeliveryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*deliveryArgs)(nil)).Elem()
}

type DeliveryInput interface {
	pulumi.Input

	ToDeliveryOutput() DeliveryOutput
	ToDeliveryOutputWithContext(ctx context.Context) DeliveryOutput
}

func (*Delivery) ElementType() reflect.Type {
	return reflect.TypeOf((**Delivery)(nil)).Elem()
}

func (i *Delivery) ToDeliveryOutput() DeliveryOutput {
	return i.ToDeliveryOutputWithContext(context.Background())
}

func (i *Delivery) ToDeliveryOutputWithContext(ctx context.Context) DeliveryOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeliveryOutput)
}

type DeliveryOutput struct{ *pulumi.OutputState }

func (DeliveryOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Delivery)(nil)).Elem()
}

func (o DeliveryOutput) ToDeliveryOutput() DeliveryOutput {
	return o
}

func (o DeliveryOutput) ToDeliveryOutputWithContext(ctx context.Context) DeliveryOutput {
	return o
}

// The Amazon Resource Name (ARN) that uniquely identifies this delivery.
func (o DeliveryOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Delivery) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The ARN of the delivery destination that is associated with this delivery.
func (o DeliveryOutput) DeliveryDestinationArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Delivery) pulumi.StringOutput { return v.DeliveryDestinationArn }).(pulumi.StringOutput)
}

// Displays whether the delivery destination associated with this delivery is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.
func (o DeliveryOutput) DeliveryDestinationType() pulumi.StringOutput {
	return o.ApplyT(func(v *Delivery) pulumi.StringOutput { return v.DeliveryDestinationType }).(pulumi.StringOutput)
}

// The unique ID that identifies this delivery in your account.
func (o DeliveryOutput) DeliveryId() pulumi.StringOutput {
	return o.ApplyT(func(v *Delivery) pulumi.StringOutput { return v.DeliveryId }).(pulumi.StringOutput)
}

// The name of the delivery source that is associated with this delivery.
func (o DeliveryOutput) DeliverySourceName() pulumi.StringOutput {
	return o.ApplyT(func(v *Delivery) pulumi.StringOutput { return v.DeliverySourceName }).(pulumi.StringOutput)
}

// The tags that have been assigned to this delivery.
func (o DeliveryOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Delivery) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DeliveryInput)(nil)).Elem(), &Delivery{})
	pulumi.RegisterOutputType(DeliveryOutput{})
}
