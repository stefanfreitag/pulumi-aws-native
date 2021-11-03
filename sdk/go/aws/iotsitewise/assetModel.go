// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iotsitewise

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::IoTSiteWise::AssetModel
type AssetModel struct {
	pulumi.CustomResourceState

	// The ARN of the asset model, which has the following format.
	AssetModelArn pulumi.StringOutput `pulumi:"assetModelArn"`
	// The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties.
	AssetModelCompositeModels AssetModelCompositeModelArrayOutput `pulumi:"assetModelCompositeModels"`
	// A description for the asset model.
	AssetModelDescription pulumi.StringPtrOutput `pulumi:"assetModelDescription"`
	// The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. You can specify up to 10 hierarchies per asset model.
	AssetModelHierarchies AssetModelHierarchyArrayOutput `pulumi:"assetModelHierarchies"`
	// The ID of the asset model.
	AssetModelId pulumi.StringOutput `pulumi:"assetModelId"`
	// A unique, friendly name for the asset model.
	AssetModelName pulumi.StringOutput `pulumi:"assetModelName"`
	// The property definitions of the asset model. You can specify up to 200 properties per asset model.
	AssetModelProperties AssetModelPropertyArrayOutput `pulumi:"assetModelProperties"`
	// A list of key-value pairs that contain metadata for the asset model.
	Tags AssetModelTagArrayOutput `pulumi:"tags"`
}

// NewAssetModel registers a new resource with the given unique name, arguments, and options.
func NewAssetModel(ctx *pulumi.Context,
	name string, args *AssetModelArgs, opts ...pulumi.ResourceOption) (*AssetModel, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AssetModelName == nil {
		return nil, errors.New("invalid value for required argument 'AssetModelName'")
	}
	var resource AssetModel
	err := ctx.RegisterResource("aws-native:iotsitewise:AssetModel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAssetModel gets an existing AssetModel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAssetModel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AssetModelState, opts ...pulumi.ResourceOption) (*AssetModel, error) {
	var resource AssetModel
	err := ctx.ReadResource("aws-native:iotsitewise:AssetModel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AssetModel resources.
type assetModelState struct {
}

type AssetModelState struct {
}

func (AssetModelState) ElementType() reflect.Type {
	return reflect.TypeOf((*assetModelState)(nil)).Elem()
}

type assetModelArgs struct {
	// The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties.
	AssetModelCompositeModels []AssetModelCompositeModel `pulumi:"assetModelCompositeModels"`
	// A description for the asset model.
	AssetModelDescription *string `pulumi:"assetModelDescription"`
	// The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. You can specify up to 10 hierarchies per asset model.
	AssetModelHierarchies []AssetModelHierarchy `pulumi:"assetModelHierarchies"`
	// A unique, friendly name for the asset model.
	AssetModelName string `pulumi:"assetModelName"`
	// The property definitions of the asset model. You can specify up to 200 properties per asset model.
	AssetModelProperties []AssetModelProperty `pulumi:"assetModelProperties"`
	// A list of key-value pairs that contain metadata for the asset model.
	Tags []AssetModelTag `pulumi:"tags"`
}

// The set of arguments for constructing a AssetModel resource.
type AssetModelArgs struct {
	// The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties.
	AssetModelCompositeModels AssetModelCompositeModelArrayInput
	// A description for the asset model.
	AssetModelDescription pulumi.StringPtrInput
	// The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. You can specify up to 10 hierarchies per asset model.
	AssetModelHierarchies AssetModelHierarchyArrayInput
	// A unique, friendly name for the asset model.
	AssetModelName pulumi.StringInput
	// The property definitions of the asset model. You can specify up to 200 properties per asset model.
	AssetModelProperties AssetModelPropertyArrayInput
	// A list of key-value pairs that contain metadata for the asset model.
	Tags AssetModelTagArrayInput
}

func (AssetModelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*assetModelArgs)(nil)).Elem()
}

type AssetModelInput interface {
	pulumi.Input

	ToAssetModelOutput() AssetModelOutput
	ToAssetModelOutputWithContext(ctx context.Context) AssetModelOutput
}

func (*AssetModel) ElementType() reflect.Type {
	return reflect.TypeOf((*AssetModel)(nil))
}

func (i *AssetModel) ToAssetModelOutput() AssetModelOutput {
	return i.ToAssetModelOutputWithContext(context.Background())
}

func (i *AssetModel) ToAssetModelOutputWithContext(ctx context.Context) AssetModelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssetModelOutput)
}

type AssetModelOutput struct{ *pulumi.OutputState }

func (AssetModelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssetModel)(nil))
}

func (o AssetModelOutput) ToAssetModelOutput() AssetModelOutput {
	return o
}

func (o AssetModelOutput) ToAssetModelOutputWithContext(ctx context.Context) AssetModelOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AssetModelInput)(nil)).Elem(), &AssetModel{})
	pulumi.RegisterOutputType(AssetModelOutput{})
}
