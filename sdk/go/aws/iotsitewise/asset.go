// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iotsitewise

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::IoTSiteWise::Asset
type Asset struct {
	pulumi.CustomResourceState

	// The ARN of the asset
	AssetArn pulumi.StringOutput `pulumi:"assetArn"`
	// A description for the asset
	AssetDescription pulumi.StringPtrOutput    `pulumi:"assetDescription"`
	AssetHierarchies AssetHierarchyArrayOutput `pulumi:"assetHierarchies"`
	// The ID of the asset
	AssetId pulumi.StringOutput `pulumi:"assetId"`
	// The ID of the asset model from which to create the asset.
	AssetModelId pulumi.StringOutput `pulumi:"assetModelId"`
	// A unique, friendly name for the asset.
	AssetName       pulumi.StringOutput      `pulumi:"assetName"`
	AssetProperties AssetPropertyArrayOutput `pulumi:"assetProperties"`
	// A list of key-value pairs that contain metadata for the asset.
	Tags AssetTagArrayOutput `pulumi:"tags"`
}

// NewAsset registers a new resource with the given unique name, arguments, and options.
func NewAsset(ctx *pulumi.Context,
	name string, args *AssetArgs, opts ...pulumi.ResourceOption) (*Asset, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AssetModelId == nil {
		return nil, errors.New("invalid value for required argument 'AssetModelId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Asset
	err := ctx.RegisterResource("aws-native:iotsitewise:Asset", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAsset gets an existing Asset resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAsset(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AssetState, opts ...pulumi.ResourceOption) (*Asset, error) {
	var resource Asset
	err := ctx.ReadResource("aws-native:iotsitewise:Asset", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Asset resources.
type assetState struct {
}

type AssetState struct {
}

func (AssetState) ElementType() reflect.Type {
	return reflect.TypeOf((*assetState)(nil)).Elem()
}

type assetArgs struct {
	// A description for the asset
	AssetDescription *string          `pulumi:"assetDescription"`
	AssetHierarchies []AssetHierarchy `pulumi:"assetHierarchies"`
	// The ID of the asset model from which to create the asset.
	AssetModelId string `pulumi:"assetModelId"`
	// A unique, friendly name for the asset.
	AssetName       *string         `pulumi:"assetName"`
	AssetProperties []AssetProperty `pulumi:"assetProperties"`
	// A list of key-value pairs that contain metadata for the asset.
	Tags []AssetTag `pulumi:"tags"`
}

// The set of arguments for constructing a Asset resource.
type AssetArgs struct {
	// A description for the asset
	AssetDescription pulumi.StringPtrInput
	AssetHierarchies AssetHierarchyArrayInput
	// The ID of the asset model from which to create the asset.
	AssetModelId pulumi.StringInput
	// A unique, friendly name for the asset.
	AssetName       pulumi.StringPtrInput
	AssetProperties AssetPropertyArrayInput
	// A list of key-value pairs that contain metadata for the asset.
	Tags AssetTagArrayInput
}

func (AssetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*assetArgs)(nil)).Elem()
}

type AssetInput interface {
	pulumi.Input

	ToAssetOutput() AssetOutput
	ToAssetOutputWithContext(ctx context.Context) AssetOutput
}

func (*Asset) ElementType() reflect.Type {
	return reflect.TypeOf((**Asset)(nil)).Elem()
}

func (i *Asset) ToAssetOutput() AssetOutput {
	return i.ToAssetOutputWithContext(context.Background())
}

func (i *Asset) ToAssetOutputWithContext(ctx context.Context) AssetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssetOutput)
}

func (i *Asset) ToOutput(ctx context.Context) pulumix.Output[*Asset] {
	return pulumix.Output[*Asset]{
		OutputState: i.ToAssetOutputWithContext(ctx).OutputState,
	}
}

type AssetOutput struct{ *pulumi.OutputState }

func (AssetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Asset)(nil)).Elem()
}

func (o AssetOutput) ToAssetOutput() AssetOutput {
	return o
}

func (o AssetOutput) ToAssetOutputWithContext(ctx context.Context) AssetOutput {
	return o
}

func (o AssetOutput) ToOutput(ctx context.Context) pulumix.Output[*Asset] {
	return pulumix.Output[*Asset]{
		OutputState: o.OutputState,
	}
}

// The ARN of the asset
func (o AssetOutput) AssetArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Asset) pulumi.StringOutput { return v.AssetArn }).(pulumi.StringOutput)
}

// A description for the asset
func (o AssetOutput) AssetDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Asset) pulumi.StringPtrOutput { return v.AssetDescription }).(pulumi.StringPtrOutput)
}

func (o AssetOutput) AssetHierarchies() AssetHierarchyArrayOutput {
	return o.ApplyT(func(v *Asset) AssetHierarchyArrayOutput { return v.AssetHierarchies }).(AssetHierarchyArrayOutput)
}

// The ID of the asset
func (o AssetOutput) AssetId() pulumi.StringOutput {
	return o.ApplyT(func(v *Asset) pulumi.StringOutput { return v.AssetId }).(pulumi.StringOutput)
}

// The ID of the asset model from which to create the asset.
func (o AssetOutput) AssetModelId() pulumi.StringOutput {
	return o.ApplyT(func(v *Asset) pulumi.StringOutput { return v.AssetModelId }).(pulumi.StringOutput)
}

// A unique, friendly name for the asset.
func (o AssetOutput) AssetName() pulumi.StringOutput {
	return o.ApplyT(func(v *Asset) pulumi.StringOutput { return v.AssetName }).(pulumi.StringOutput)
}

func (o AssetOutput) AssetProperties() AssetPropertyArrayOutput {
	return o.ApplyT(func(v *Asset) AssetPropertyArrayOutput { return v.AssetProperties }).(AssetPropertyArrayOutput)
}

// A list of key-value pairs that contain metadata for the asset.
func (o AssetOutput) Tags() AssetTagArrayOutput {
	return o.ApplyT(func(v *Asset) AssetTagArrayOutput { return v.Tags }).(AssetTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AssetInput)(nil)).Elem(), &Asset{})
	pulumi.RegisterOutputType(AssetOutput{})
}
