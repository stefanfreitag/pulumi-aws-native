// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package s3outposts

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type Definition for AWS::S3Outposts::BucketPolicy
type BucketPolicy struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the specified bucket.
	Bucket pulumi.StringOutput `pulumi:"bucket"`
	// A policy document containing permissions to add to the specified bucket.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::S3Outposts::BucketPolicy` for more information about the expected schema for this property.
	PolicyDocument pulumi.AnyOutput `pulumi:"policyDocument"`
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
	err := ctx.RegisterResource("aws-native:s3outposts:BucketPolicy", name, args, &resource, opts...)
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
	err := ctx.ReadResource("aws-native:s3outposts:BucketPolicy", name, id, state, &resource, opts...)
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
	// The Amazon Resource Name (ARN) of the specified bucket.
	Bucket string `pulumi:"bucket"`
	// A policy document containing permissions to add to the specified bucket.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::S3Outposts::BucketPolicy` for more information about the expected schema for this property.
	PolicyDocument interface{} `pulumi:"policyDocument"`
}

// The set of arguments for constructing a BucketPolicy resource.
type BucketPolicyArgs struct {
	// The Amazon Resource Name (ARN) of the specified bucket.
	Bucket pulumi.StringInput
	// A policy document containing permissions to add to the specified bucket.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::S3Outposts::BucketPolicy` for more information about the expected schema for this property.
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

// The Amazon Resource Name (ARN) of the specified bucket.
func (o BucketPolicyOutput) Bucket() pulumi.StringOutput {
	return o.ApplyT(func(v *BucketPolicy) pulumi.StringOutput { return v.Bucket }).(pulumi.StringOutput)
}

// A policy document containing permissions to add to the specified bucket.
//
// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::S3Outposts::BucketPolicy` for more information about the expected schema for this property.
func (o BucketPolicyOutput) PolicyDocument() pulumi.AnyOutput {
	return o.ApplyT(func(v *BucketPolicy) pulumi.AnyOutput { return v.PolicyDocument }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*BucketPolicyInput)(nil)).Elem(), &BucketPolicy{})
	pulumi.RegisterOutputType(BucketPolicyOutput{})
}
