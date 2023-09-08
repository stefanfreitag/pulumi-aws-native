// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package datasync

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::DataSync::LocationS3
type LocationS3 struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the Amazon S3 bucket location.
	LocationArn pulumi.StringOutput `pulumi:"locationArn"`
	// The URL of the S3 location that was described.
	LocationUri pulumi.StringOutput `pulumi:"locationUri"`
	// The Amazon Resource Name (ARN) of the Amazon S3 bucket.
	S3BucketArn pulumi.StringPtrOutput   `pulumi:"s3BucketArn"`
	S3Config    LocationS3s3ConfigOutput `pulumi:"s3Config"`
	// The Amazon S3 storage class you want to store your files in when this location is used as a task destination.
	S3StorageClass LocationS3S3StorageClassPtrOutput `pulumi:"s3StorageClass"`
	// A subdirectory in the Amazon S3 bucket. This subdirectory in Amazon S3 is used to read data from the S3 source location or write data to the S3 destination.
	Subdirectory pulumi.StringPtrOutput `pulumi:"subdirectory"`
	// An array of key-value pairs to apply to this resource.
	Tags LocationS3TagArrayOutput `pulumi:"tags"`
}

// NewLocationS3 registers a new resource with the given unique name, arguments, and options.
func NewLocationS3(ctx *pulumi.Context,
	name string, args *LocationS3Args, opts ...pulumi.ResourceOption) (*LocationS3, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.S3Config == nil {
		return nil, errors.New("invalid value for required argument 'S3Config'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"s3BucketArn",
		"s3Config",
		"s3StorageClass",
		"subdirectory",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource LocationS3
	err := ctx.RegisterResource("aws-native:datasync:LocationS3", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLocationS3 gets an existing LocationS3 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLocationS3(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LocationS3State, opts ...pulumi.ResourceOption) (*LocationS3, error) {
	var resource LocationS3
	err := ctx.ReadResource("aws-native:datasync:LocationS3", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LocationS3 resources.
type locationS3State struct {
}

type LocationS3State struct {
}

func (LocationS3State) ElementType() reflect.Type {
	return reflect.TypeOf((*locationS3State)(nil)).Elem()
}

type locationS3Args struct {
	// The Amazon Resource Name (ARN) of the Amazon S3 bucket.
	S3BucketArn *string            `pulumi:"s3BucketArn"`
	S3Config    LocationS3s3Config `pulumi:"s3Config"`
	// The Amazon S3 storage class you want to store your files in when this location is used as a task destination.
	S3StorageClass *LocationS3S3StorageClass `pulumi:"s3StorageClass"`
	// A subdirectory in the Amazon S3 bucket. This subdirectory in Amazon S3 is used to read data from the S3 source location or write data to the S3 destination.
	Subdirectory *string `pulumi:"subdirectory"`
	// An array of key-value pairs to apply to this resource.
	Tags []LocationS3Tag `pulumi:"tags"`
}

// The set of arguments for constructing a LocationS3 resource.
type LocationS3Args struct {
	// The Amazon Resource Name (ARN) of the Amazon S3 bucket.
	S3BucketArn pulumi.StringPtrInput
	S3Config    LocationS3s3ConfigInput
	// The Amazon S3 storage class you want to store your files in when this location is used as a task destination.
	S3StorageClass LocationS3S3StorageClassPtrInput
	// A subdirectory in the Amazon S3 bucket. This subdirectory in Amazon S3 is used to read data from the S3 source location or write data to the S3 destination.
	Subdirectory pulumi.StringPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags LocationS3TagArrayInput
}

func (LocationS3Args) ElementType() reflect.Type {
	return reflect.TypeOf((*locationS3Args)(nil)).Elem()
}

type LocationS3Input interface {
	pulumi.Input

	ToLocationS3Output() LocationS3Output
	ToLocationS3OutputWithContext(ctx context.Context) LocationS3Output
}

func (*LocationS3) ElementType() reflect.Type {
	return reflect.TypeOf((**LocationS3)(nil)).Elem()
}

func (i *LocationS3) ToLocationS3Output() LocationS3Output {
	return i.ToLocationS3OutputWithContext(context.Background())
}

func (i *LocationS3) ToLocationS3OutputWithContext(ctx context.Context) LocationS3Output {
	return pulumi.ToOutputWithContext(ctx, i).(LocationS3Output)
}

func (i *LocationS3) ToOutput(ctx context.Context) pulumix.Output[*LocationS3] {
	return pulumix.Output[*LocationS3]{
		OutputState: i.ToLocationS3OutputWithContext(ctx).OutputState,
	}
}

type LocationS3Output struct{ *pulumi.OutputState }

func (LocationS3Output) ElementType() reflect.Type {
	return reflect.TypeOf((**LocationS3)(nil)).Elem()
}

func (o LocationS3Output) ToLocationS3Output() LocationS3Output {
	return o
}

func (o LocationS3Output) ToLocationS3OutputWithContext(ctx context.Context) LocationS3Output {
	return o
}

func (o LocationS3Output) ToOutput(ctx context.Context) pulumix.Output[*LocationS3] {
	return pulumix.Output[*LocationS3]{
		OutputState: o.OutputState,
	}
}

// The Amazon Resource Name (ARN) of the Amazon S3 bucket location.
func (o LocationS3Output) LocationArn() pulumi.StringOutput {
	return o.ApplyT(func(v *LocationS3) pulumi.StringOutput { return v.LocationArn }).(pulumi.StringOutput)
}

// The URL of the S3 location that was described.
func (o LocationS3Output) LocationUri() pulumi.StringOutput {
	return o.ApplyT(func(v *LocationS3) pulumi.StringOutput { return v.LocationUri }).(pulumi.StringOutput)
}

// The Amazon Resource Name (ARN) of the Amazon S3 bucket.
func (o LocationS3Output) S3BucketArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LocationS3) pulumi.StringPtrOutput { return v.S3BucketArn }).(pulumi.StringPtrOutput)
}

func (o LocationS3Output) S3Config() LocationS3s3ConfigOutput {
	return o.ApplyT(func(v *LocationS3) LocationS3s3ConfigOutput { return v.S3Config }).(LocationS3s3ConfigOutput)
}

// The Amazon S3 storage class you want to store your files in when this location is used as a task destination.
func (o LocationS3Output) S3StorageClass() LocationS3S3StorageClassPtrOutput {
	return o.ApplyT(func(v *LocationS3) LocationS3S3StorageClassPtrOutput { return v.S3StorageClass }).(LocationS3S3StorageClassPtrOutput)
}

// A subdirectory in the Amazon S3 bucket. This subdirectory in Amazon S3 is used to read data from the S3 source location or write data to the S3 destination.
func (o LocationS3Output) Subdirectory() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LocationS3) pulumi.StringPtrOutput { return v.Subdirectory }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LocationS3Output) Tags() LocationS3TagArrayOutput {
	return o.ApplyT(func(v *LocationS3) LocationS3TagArrayOutput { return v.Tags }).(LocationS3TagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LocationS3Input)(nil)).Elem(), &LocationS3{})
	pulumi.RegisterOutputType(LocationS3Output{})
}
