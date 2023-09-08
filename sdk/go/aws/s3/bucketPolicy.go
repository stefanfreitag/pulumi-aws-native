// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package s3

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::S3::BucketPolicy
//
// Deprecated: BucketPolicy is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type BucketPolicy struct {
	pulumi.CustomResourceState

	Bucket         pulumi.StringOutput `pulumi:"bucket"`
	PolicyDocument pulumi.AnyOutput    `pulumi:"policyDocument"`
}

// NewBucketPolicy registers a new resource with the given unique name, arguments, and options.
func NewBucketPolicy(ctx *pulumi.Context,
	name string, args *BucketPolicyArgs, opts ...pulumi.ResourceOption) (*BucketPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Bucket == nil {
		return nil, errors.New("invalid value for required argument 'Bucket'")
	}
	if args.PolicyDocument == nil {
		return nil, errors.New("invalid value for required argument 'PolicyDocument'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"bucket",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource BucketPolicy
	err := ctx.RegisterResource("aws-native:s3:BucketPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBucketPolicy gets an existing BucketPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBucketPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BucketPolicyState, opts ...pulumi.ResourceOption) (*BucketPolicy, error) {
	var resource BucketPolicy
	err := ctx.ReadResource("aws-native:s3:BucketPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BucketPolicy resources.
type bucketPolicyState struct {
}

type BucketPolicyState struct {
}

func (BucketPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*bucketPolicyState)(nil)).Elem()
}

type bucketPolicyArgs struct {
	Bucket         string      `pulumi:"bucket"`
	PolicyDocument interface{} `pulumi:"policyDocument"`
}

// The set of arguments for constructing a BucketPolicy resource.
type BucketPolicyArgs struct {
	Bucket         pulumi.StringInput
	PolicyDocument pulumi.Input
}

func (BucketPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*bucketPolicyArgs)(nil)).Elem()
}

type BucketPolicyInput interface {
	pulumi.Input

	ToBucketPolicyOutput() BucketPolicyOutput
	ToBucketPolicyOutputWithContext(ctx context.Context) BucketPolicyOutput
}

func (*BucketPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((**BucketPolicy)(nil)).Elem()
}

func (i *BucketPolicy) ToBucketPolicyOutput() BucketPolicyOutput {
	return i.ToBucketPolicyOutputWithContext(context.Background())
}

func (i *BucketPolicy) ToBucketPolicyOutputWithContext(ctx context.Context) BucketPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BucketPolicyOutput)
}

func (i *BucketPolicy) ToOutput(ctx context.Context) pulumix.Output[*BucketPolicy] {
	return pulumix.Output[*BucketPolicy]{
		OutputState: i.ToBucketPolicyOutputWithContext(ctx).OutputState,
	}
}

type BucketPolicyOutput struct{ *pulumi.OutputState }

func (BucketPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**BucketPolicy)(nil)).Elem()
}

func (o BucketPolicyOutput) ToBucketPolicyOutput() BucketPolicyOutput {
	return o
}

func (o BucketPolicyOutput) ToBucketPolicyOutputWithContext(ctx context.Context) BucketPolicyOutput {
	return o
}

func (o BucketPolicyOutput) ToOutput(ctx context.Context) pulumix.Output[*BucketPolicy] {
	return pulumix.Output[*BucketPolicy]{
		OutputState: o.OutputState,
	}
}

func (o BucketPolicyOutput) Bucket() pulumi.StringOutput {
	return o.ApplyT(func(v *BucketPolicy) pulumi.StringOutput { return v.Bucket }).(pulumi.StringOutput)
}

func (o BucketPolicyOutput) PolicyDocument() pulumi.AnyOutput {
	return o.ApplyT(func(v *BucketPolicy) pulumi.AnyOutput { return v.PolicyDocument }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*BucketPolicyInput)(nil)).Elem(), &BucketPolicy{})
	pulumi.RegisterOutputType(BucketPolicyOutput{})
}
