// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lightsail

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Lightsail::Bucket
type Bucket struct {
	pulumi.CustomResourceState

	// Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle. You can update a bucket's bundle only one time within a monthly AWS billing cycle.
	AbleToUpdateBundle pulumi.BoolOutput          `pulumi:"ableToUpdateBundle"`
	AccessRules        BucketAccessRulesPtrOutput `pulumi:"accessRules"`
	BucketArn          pulumi.StringOutput        `pulumi:"bucketArn"`
	// The name for the bucket.
	BucketName pulumi.StringOutput `pulumi:"bucketName"`
	// The ID of the bundle to use for the bucket.
	BundleId pulumi.StringOutput `pulumi:"bundleId"`
	// Specifies whether to enable or disable versioning of objects in the bucket.
	ObjectVersioning pulumi.BoolPtrOutput `pulumi:"objectVersioning"`
	// An array of strings to specify the AWS account IDs that can access the bucket.
	ReadOnlyAccessAccounts pulumi.StringArrayOutput `pulumi:"readOnlyAccessAccounts"`
	// The names of the Lightsail resources for which to set bucket access.
	ResourcesReceivingAccess pulumi.StringArrayOutput `pulumi:"resourcesReceivingAccess"`
	// An array of key-value pairs to apply to this resource.
	Tags BucketTagArrayOutput `pulumi:"tags"`
	// The URL of the bucket.
	Url pulumi.StringOutput `pulumi:"url"`
}

// NewBucket registers a new resource with the given unique name, arguments, and options.
func NewBucket(ctx *pulumi.Context,
	name string, args *BucketArgs, opts ...pulumi.ResourceOption) (*Bucket, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.BundleId == nil {
		return nil, errors.New("invalid value for required argument 'BundleId'")
	}
	var resource Bucket
	err := ctx.RegisterResource("aws-native:lightsail:Bucket", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBucket gets an existing Bucket resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBucket(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BucketState, opts ...pulumi.ResourceOption) (*Bucket, error) {
	var resource Bucket
	err := ctx.ReadResource("aws-native:lightsail:Bucket", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Bucket resources.
type bucketState struct {
}

type BucketState struct {
}

func (BucketState) ElementType() reflect.Type {
	return reflect.TypeOf((*bucketState)(nil)).Elem()
}

type bucketArgs struct {
	AccessRules *BucketAccessRules `pulumi:"accessRules"`
	// The name for the bucket.
	BucketName *string `pulumi:"bucketName"`
	// The ID of the bundle to use for the bucket.
	BundleId string `pulumi:"bundleId"`
	// Specifies whether to enable or disable versioning of objects in the bucket.
	ObjectVersioning *bool `pulumi:"objectVersioning"`
	// An array of strings to specify the AWS account IDs that can access the bucket.
	ReadOnlyAccessAccounts []string `pulumi:"readOnlyAccessAccounts"`
	// The names of the Lightsail resources for which to set bucket access.
	ResourcesReceivingAccess []string `pulumi:"resourcesReceivingAccess"`
	// An array of key-value pairs to apply to this resource.
	Tags []BucketTag `pulumi:"tags"`
}

// The set of arguments for constructing a Bucket resource.
type BucketArgs struct {
	AccessRules BucketAccessRulesPtrInput
	// The name for the bucket.
	BucketName pulumi.StringPtrInput
	// The ID of the bundle to use for the bucket.
	BundleId pulumi.StringInput
	// Specifies whether to enable or disable versioning of objects in the bucket.
	ObjectVersioning pulumi.BoolPtrInput
	// An array of strings to specify the AWS account IDs that can access the bucket.
	ReadOnlyAccessAccounts pulumi.StringArrayInput
	// The names of the Lightsail resources for which to set bucket access.
	ResourcesReceivingAccess pulumi.StringArrayInput
	// An array of key-value pairs to apply to this resource.
	Tags BucketTagArrayInput
}

func (BucketArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*bucketArgs)(nil)).Elem()
}

type BucketInput interface {
	pulumi.Input

	ToBucketOutput() BucketOutput
	ToBucketOutputWithContext(ctx context.Context) BucketOutput
}

func (*Bucket) ElementType() reflect.Type {
	return reflect.TypeOf((**Bucket)(nil)).Elem()
}

func (i *Bucket) ToBucketOutput() BucketOutput {
	return i.ToBucketOutputWithContext(context.Background())
}

func (i *Bucket) ToBucketOutputWithContext(ctx context.Context) BucketOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BucketOutput)
}

type BucketOutput struct{ *pulumi.OutputState }

func (BucketOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Bucket)(nil)).Elem()
}

func (o BucketOutput) ToBucketOutput() BucketOutput {
	return o
}

func (o BucketOutput) ToBucketOutputWithContext(ctx context.Context) BucketOutput {
	return o
}

// Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle. You can update a bucket's bundle only one time within a monthly AWS billing cycle.
func (o BucketOutput) AbleToUpdateBundle() pulumi.BoolOutput {
	return o.ApplyT(func(v *Bucket) pulumi.BoolOutput { return v.AbleToUpdateBundle }).(pulumi.BoolOutput)
}

func (o BucketOutput) AccessRules() BucketAccessRulesPtrOutput {
	return o.ApplyT(func(v *Bucket) BucketAccessRulesPtrOutput { return v.AccessRules }).(BucketAccessRulesPtrOutput)
}

func (o BucketOutput) BucketArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Bucket) pulumi.StringOutput { return v.BucketArn }).(pulumi.StringOutput)
}

// The name for the bucket.
func (o BucketOutput) BucketName() pulumi.StringOutput {
	return o.ApplyT(func(v *Bucket) pulumi.StringOutput { return v.BucketName }).(pulumi.StringOutput)
}

// The ID of the bundle to use for the bucket.
func (o BucketOutput) BundleId() pulumi.StringOutput {
	return o.ApplyT(func(v *Bucket) pulumi.StringOutput { return v.BundleId }).(pulumi.StringOutput)
}

// Specifies whether to enable or disable versioning of objects in the bucket.
func (o BucketOutput) ObjectVersioning() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Bucket) pulumi.BoolPtrOutput { return v.ObjectVersioning }).(pulumi.BoolPtrOutput)
}

// An array of strings to specify the AWS account IDs that can access the bucket.
func (o BucketOutput) ReadOnlyAccessAccounts() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Bucket) pulumi.StringArrayOutput { return v.ReadOnlyAccessAccounts }).(pulumi.StringArrayOutput)
}

// The names of the Lightsail resources for which to set bucket access.
func (o BucketOutput) ResourcesReceivingAccess() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Bucket) pulumi.StringArrayOutput { return v.ResourcesReceivingAccess }).(pulumi.StringArrayOutput)
}

// An array of key-value pairs to apply to this resource.
func (o BucketOutput) Tags() BucketTagArrayOutput {
	return o.ApplyT(func(v *Bucket) BucketTagArrayOutput { return v.Tags }).(BucketTagArrayOutput)
}

// The URL of the bucket.
func (o BucketOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v *Bucket) pulumi.StringOutput { return v.Url }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*BucketInput)(nil)).Elem(), &Bucket{})
	pulumi.RegisterOutputType(BucketOutput{})
}
