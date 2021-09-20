// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudfront

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CloudFront::CachePolicy
type CachePolicy struct {
	pulumi.CustomResourceState

	CachePolicyConfig CachePolicyCachePolicyConfigOutput `pulumi:"cachePolicyConfig"`
	LastModifiedTime  pulumi.StringOutput                `pulumi:"lastModifiedTime"`
}

// NewCachePolicy registers a new resource with the given unique name, arguments, and options.
func NewCachePolicy(ctx *pulumi.Context,
	name string, args *CachePolicyArgs, opts ...pulumi.ResourceOption) (*CachePolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CachePolicyConfig == nil {
		return nil, errors.New("invalid value for required argument 'CachePolicyConfig'")
	}
	var resource CachePolicy
	err := ctx.RegisterResource("aws-native:cloudfront:CachePolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCachePolicy gets an existing CachePolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCachePolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CachePolicyState, opts ...pulumi.ResourceOption) (*CachePolicy, error) {
	var resource CachePolicy
	err := ctx.ReadResource("aws-native:cloudfront:CachePolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CachePolicy resources.
type cachePolicyState struct {
}

type CachePolicyState struct {
}

func (CachePolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*cachePolicyState)(nil)).Elem()
}

type cachePolicyArgs struct {
	CachePolicyConfig CachePolicyCachePolicyConfig `pulumi:"cachePolicyConfig"`
}

// The set of arguments for constructing a CachePolicy resource.
type CachePolicyArgs struct {
	CachePolicyConfig CachePolicyCachePolicyConfigInput
}

func (CachePolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cachePolicyArgs)(nil)).Elem()
}

type CachePolicyInput interface {
	pulumi.Input

	ToCachePolicyOutput() CachePolicyOutput
	ToCachePolicyOutputWithContext(ctx context.Context) CachePolicyOutput
}

func (*CachePolicy) ElementType() reflect.Type {
	return reflect.TypeOf((*CachePolicy)(nil))
}

func (i *CachePolicy) ToCachePolicyOutput() CachePolicyOutput {
	return i.ToCachePolicyOutputWithContext(context.Background())
}

func (i *CachePolicy) ToCachePolicyOutputWithContext(ctx context.Context) CachePolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CachePolicyOutput)
}

type CachePolicyOutput struct{ *pulumi.OutputState }

func (CachePolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CachePolicy)(nil))
}

func (o CachePolicyOutput) ToCachePolicyOutput() CachePolicyOutput {
	return o
}

func (o CachePolicyOutput) ToCachePolicyOutputWithContext(ctx context.Context) CachePolicyOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(CachePolicyOutput{})
}
