// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package kendra

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html
type Index struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-capacityunits
	CapacityUnits IndexCapacityUnitsConfigurationPtrOutput `pulumi:"capacityUnits"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-description
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-documentmetadataconfigurations
	DocumentMetadataConfigurations IndexDocumentMetadataConfigurationListPtrOutput `pulumi:"documentMetadataConfigurations"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-edition
	Edition pulumi.StringOutput `pulumi:"edition"`
	Id      pulumi.StringOutput `pulumi:"id"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-name
	Name pulumi.StringOutput `pulumi:"name"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-rolearn
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-serversideencryptionconfiguration
	ServerSideEncryptionConfiguration IndexServerSideEncryptionConfigurationPtrOutput `pulumi:"serverSideEncryptionConfiguration"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-tags
	Tags IndexTagListPtrOutput `pulumi:"tags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usercontextpolicy
	UserContextPolicy pulumi.StringPtrOutput `pulumi:"userContextPolicy"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usertokenconfigurations
	UserTokenConfigurations IndexUserTokenConfigurationListPtrOutput `pulumi:"userTokenConfigurations"`
}

// NewIndex registers a new resource with the given unique name, arguments, and options.
func NewIndex(ctx *pulumi.Context,
	name string, args *IndexArgs, opts ...pulumi.ResourceOption) (*Index, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Edition == nil {
		return nil, errors.New("invalid value for required argument 'Edition'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	var resource Index
	err := ctx.RegisterResource("aws-native:Kendra:Index", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIndex gets an existing Index resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIndex(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IndexState, opts ...pulumi.ResourceOption) (*Index, error) {
	var resource Index
	err := ctx.ReadResource("aws-native:Kendra:Index", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Index resources.
type indexState struct {
}

type IndexState struct {
}

func (IndexState) ElementType() reflect.Type {
	return reflect.TypeOf((*indexState)(nil)).Elem()
}

type indexArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-capacityunits
	CapacityUnits *IndexCapacityUnitsConfiguration `pulumi:"capacityUnits"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-description
	Description *string `pulumi:"description"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-documentmetadataconfigurations
	DocumentMetadataConfigurations *IndexDocumentMetadataConfigurationList `pulumi:"documentMetadataConfigurations"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-edition
	Edition string `pulumi:"edition"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-name
	Name string `pulumi:"name"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-rolearn
	RoleArn string `pulumi:"roleArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-serversideencryptionconfiguration
	ServerSideEncryptionConfiguration *IndexServerSideEncryptionConfiguration `pulumi:"serverSideEncryptionConfiguration"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-tags
	Tags *IndexTagList `pulumi:"tags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usercontextpolicy
	UserContextPolicy *string `pulumi:"userContextPolicy"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usertokenconfigurations
	UserTokenConfigurations *IndexUserTokenConfigurationList `pulumi:"userTokenConfigurations"`
}

// The set of arguments for constructing a Index resource.
type IndexArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-capacityunits
	CapacityUnits IndexCapacityUnitsConfigurationPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-description
	Description pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-documentmetadataconfigurations
	DocumentMetadataConfigurations IndexDocumentMetadataConfigurationListPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-edition
	Edition pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-name
	Name pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-rolearn
	RoleArn pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-serversideencryptionconfiguration
	ServerSideEncryptionConfiguration IndexServerSideEncryptionConfigurationPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-tags
	Tags IndexTagListPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usercontextpolicy
	UserContextPolicy pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usertokenconfigurations
	UserTokenConfigurations IndexUserTokenConfigurationListPtrInput
}

func (IndexArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*indexArgs)(nil)).Elem()
}

type IndexInput interface {
	pulumi.Input

	ToIndexOutput() IndexOutput
	ToIndexOutputWithContext(ctx context.Context) IndexOutput
}

func (*Index) ElementType() reflect.Type {
	return reflect.TypeOf((*Index)(nil))
}

func (i *Index) ToIndexOutput() IndexOutput {
	return i.ToIndexOutputWithContext(context.Background())
}

func (i *Index) ToIndexOutputWithContext(ctx context.Context) IndexOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IndexOutput)
}

type IndexOutput struct{ *pulumi.OutputState }

func (IndexOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Index)(nil))
}

func (o IndexOutput) ToIndexOutput() IndexOutput {
	return o
}

func (o IndexOutput) ToIndexOutputWithContext(ctx context.Context) IndexOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(IndexOutput{})
}
