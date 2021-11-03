// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pinpoint

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Pinpoint::Segment
//
// Deprecated: Segment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Segment struct {
	pulumi.CustomResourceState

	ApplicationId pulumi.StringOutput        `pulumi:"applicationId"`
	Arn           pulumi.StringOutput        `pulumi:"arn"`
	Dimensions    SegmentDimensionsPtrOutput `pulumi:"dimensions"`
	Name          pulumi.StringOutput        `pulumi:"name"`
	SegmentGroups SegmentGroupsPtrOutput     `pulumi:"segmentGroups"`
	SegmentId     pulumi.StringOutput        `pulumi:"segmentId"`
	Tags          pulumi.AnyOutput           `pulumi:"tags"`
}

// NewSegment registers a new resource with the given unique name, arguments, and options.
func NewSegment(ctx *pulumi.Context,
	name string, args *SegmentArgs, opts ...pulumi.ResourceOption) (*Segment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApplicationId == nil {
		return nil, errors.New("invalid value for required argument 'ApplicationId'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource Segment
	err := ctx.RegisterResource("aws-native:pinpoint:Segment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSegment gets an existing Segment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSegment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SegmentState, opts ...pulumi.ResourceOption) (*Segment, error) {
	var resource Segment
	err := ctx.ReadResource("aws-native:pinpoint:Segment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Segment resources.
type segmentState struct {
}

type SegmentState struct {
}

func (SegmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*segmentState)(nil)).Elem()
}

type segmentArgs struct {
	ApplicationId string             `pulumi:"applicationId"`
	Dimensions    *SegmentDimensions `pulumi:"dimensions"`
	Name          string             `pulumi:"name"`
	SegmentGroups *SegmentGroups     `pulumi:"segmentGroups"`
	Tags          interface{}        `pulumi:"tags"`
}

// The set of arguments for constructing a Segment resource.
type SegmentArgs struct {
	ApplicationId pulumi.StringInput
	Dimensions    SegmentDimensionsPtrInput
	Name          pulumi.StringInput
	SegmentGroups SegmentGroupsPtrInput
	Tags          pulumi.Input
}

func (SegmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*segmentArgs)(nil)).Elem()
}

type SegmentInput interface {
	pulumi.Input

	ToSegmentOutput() SegmentOutput
	ToSegmentOutputWithContext(ctx context.Context) SegmentOutput
}

func (*Segment) ElementType() reflect.Type {
	return reflect.TypeOf((*Segment)(nil))
}

func (i *Segment) ToSegmentOutput() SegmentOutput {
	return i.ToSegmentOutputWithContext(context.Background())
}

func (i *Segment) ToSegmentOutputWithContext(ctx context.Context) SegmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SegmentOutput)
}

type SegmentOutput struct{ *pulumi.OutputState }

func (SegmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Segment)(nil))
}

func (o SegmentOutput) ToSegmentOutput() SegmentOutput {
	return o
}

func (o SegmentOutput) ToSegmentOutputWithContext(ctx context.Context) SegmentOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SegmentInput)(nil)).Elem(), &Segment{})
	pulumi.RegisterOutputType(SegmentOutput{})
}
