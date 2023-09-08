// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudfront

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::CloudFront::StreamingDistribution
//
// Deprecated: StreamingDistribution is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type StreamingDistribution struct {
	pulumi.CustomResourceState

	DomainName                  pulumi.StringOutput                 `pulumi:"domainName"`
	StreamingDistributionConfig StreamingDistributionConfigOutput   `pulumi:"streamingDistributionConfig"`
	Tags                        StreamingDistributionTagArrayOutput `pulumi:"tags"`
}

// NewStreamingDistribution registers a new resource with the given unique name, arguments, and options.
func NewStreamingDistribution(ctx *pulumi.Context,
	name string, args *StreamingDistributionArgs, opts ...pulumi.ResourceOption) (*StreamingDistribution, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.StreamingDistributionConfig == nil {
		return nil, errors.New("invalid value for required argument 'StreamingDistributionConfig'")
	}
	if args.Tags == nil {
		return nil, errors.New("invalid value for required argument 'Tags'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource StreamingDistribution
	err := ctx.RegisterResource("aws-native:cloudfront:StreamingDistribution", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStreamingDistribution gets an existing StreamingDistribution resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStreamingDistribution(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StreamingDistributionState, opts ...pulumi.ResourceOption) (*StreamingDistribution, error) {
	var resource StreamingDistribution
	err := ctx.ReadResource("aws-native:cloudfront:StreamingDistribution", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StreamingDistribution resources.
type streamingDistributionState struct {
}

type StreamingDistributionState struct {
}

func (StreamingDistributionState) ElementType() reflect.Type {
	return reflect.TypeOf((*streamingDistributionState)(nil)).Elem()
}

type streamingDistributionArgs struct {
	StreamingDistributionConfig StreamingDistributionConfig `pulumi:"streamingDistributionConfig"`
	Tags                        []StreamingDistributionTag  `pulumi:"tags"`
}

// The set of arguments for constructing a StreamingDistribution resource.
type StreamingDistributionArgs struct {
	StreamingDistributionConfig StreamingDistributionConfigInput
	Tags                        StreamingDistributionTagArrayInput
}

func (StreamingDistributionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*streamingDistributionArgs)(nil)).Elem()
}

type StreamingDistributionInput interface {
	pulumi.Input

	ToStreamingDistributionOutput() StreamingDistributionOutput
	ToStreamingDistributionOutputWithContext(ctx context.Context) StreamingDistributionOutput
}

func (*StreamingDistribution) ElementType() reflect.Type {
	return reflect.TypeOf((**StreamingDistribution)(nil)).Elem()
}

func (i *StreamingDistribution) ToStreamingDistributionOutput() StreamingDistributionOutput {
	return i.ToStreamingDistributionOutputWithContext(context.Background())
}

func (i *StreamingDistribution) ToStreamingDistributionOutputWithContext(ctx context.Context) StreamingDistributionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StreamingDistributionOutput)
}

func (i *StreamingDistribution) ToOutput(ctx context.Context) pulumix.Output[*StreamingDistribution] {
	return pulumix.Output[*StreamingDistribution]{
		OutputState: i.ToStreamingDistributionOutputWithContext(ctx).OutputState,
	}
}

type StreamingDistributionOutput struct{ *pulumi.OutputState }

func (StreamingDistributionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StreamingDistribution)(nil)).Elem()
}

func (o StreamingDistributionOutput) ToStreamingDistributionOutput() StreamingDistributionOutput {
	return o
}

func (o StreamingDistributionOutput) ToStreamingDistributionOutputWithContext(ctx context.Context) StreamingDistributionOutput {
	return o
}

func (o StreamingDistributionOutput) ToOutput(ctx context.Context) pulumix.Output[*StreamingDistribution] {
	return pulumix.Output[*StreamingDistribution]{
		OutputState: o.OutputState,
	}
}

func (o StreamingDistributionOutput) DomainName() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamingDistribution) pulumi.StringOutput { return v.DomainName }).(pulumi.StringOutput)
}

func (o StreamingDistributionOutput) StreamingDistributionConfig() StreamingDistributionConfigOutput {
	return o.ApplyT(func(v *StreamingDistribution) StreamingDistributionConfigOutput { return v.StreamingDistributionConfig }).(StreamingDistributionConfigOutput)
}

func (o StreamingDistributionOutput) Tags() StreamingDistributionTagArrayOutput {
	return o.ApplyT(func(v *StreamingDistribution) StreamingDistributionTagArrayOutput { return v.Tags }).(StreamingDistributionTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StreamingDistributionInput)(nil)).Elem(), &StreamingDistribution{})
	pulumi.RegisterOutputType(StreamingDistributionOutput{})
}
