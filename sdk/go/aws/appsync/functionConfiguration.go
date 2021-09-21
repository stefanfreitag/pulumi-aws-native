// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appsync

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AppSync::FunctionConfiguration
//
// Deprecated: FunctionConfiguration is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type FunctionConfiguration struct {
	pulumi.CustomResourceState

	ApiId                             pulumi.StringOutput                      `pulumi:"apiId"`
	DataSourceName                    pulumi.StringOutput                      `pulumi:"dataSourceName"`
	Description                       pulumi.StringPtrOutput                   `pulumi:"description"`
	FunctionArn                       pulumi.StringOutput                      `pulumi:"functionArn"`
	FunctionId                        pulumi.StringOutput                      `pulumi:"functionId"`
	FunctionVersion                   pulumi.StringOutput                      `pulumi:"functionVersion"`
	Name                              pulumi.StringOutput                      `pulumi:"name"`
	RequestMappingTemplate            pulumi.StringPtrOutput                   `pulumi:"requestMappingTemplate"`
	RequestMappingTemplateS3Location  pulumi.StringPtrOutput                   `pulumi:"requestMappingTemplateS3Location"`
	ResponseMappingTemplate           pulumi.StringPtrOutput                   `pulumi:"responseMappingTemplate"`
	ResponseMappingTemplateS3Location pulumi.StringPtrOutput                   `pulumi:"responseMappingTemplateS3Location"`
	SyncConfig                        FunctionConfigurationSyncConfigPtrOutput `pulumi:"syncConfig"`
}

// NewFunctionConfiguration registers a new resource with the given unique name, arguments, and options.
func NewFunctionConfiguration(ctx *pulumi.Context,
	name string, args *FunctionConfigurationArgs, opts ...pulumi.ResourceOption) (*FunctionConfiguration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApiId == nil {
		return nil, errors.New("invalid value for required argument 'ApiId'")
	}
	if args.DataSourceName == nil {
		return nil, errors.New("invalid value for required argument 'DataSourceName'")
	}
	if args.FunctionVersion == nil {
		return nil, errors.New("invalid value for required argument 'FunctionVersion'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource FunctionConfiguration
	err := ctx.RegisterResource("aws-native:appsync:FunctionConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFunctionConfiguration gets an existing FunctionConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFunctionConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FunctionConfigurationState, opts ...pulumi.ResourceOption) (*FunctionConfiguration, error) {
	var resource FunctionConfiguration
	err := ctx.ReadResource("aws-native:appsync:FunctionConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FunctionConfiguration resources.
type functionConfigurationState struct {
}

type FunctionConfigurationState struct {
}

func (FunctionConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*functionConfigurationState)(nil)).Elem()
}

type functionConfigurationArgs struct {
	ApiId                             string                           `pulumi:"apiId"`
	DataSourceName                    string                           `pulumi:"dataSourceName"`
	Description                       *string                          `pulumi:"description"`
	FunctionVersion                   string                           `pulumi:"functionVersion"`
	Name                              string                           `pulumi:"name"`
	RequestMappingTemplate            *string                          `pulumi:"requestMappingTemplate"`
	RequestMappingTemplateS3Location  *string                          `pulumi:"requestMappingTemplateS3Location"`
	ResponseMappingTemplate           *string                          `pulumi:"responseMappingTemplate"`
	ResponseMappingTemplateS3Location *string                          `pulumi:"responseMappingTemplateS3Location"`
	SyncConfig                        *FunctionConfigurationSyncConfig `pulumi:"syncConfig"`
}

// The set of arguments for constructing a FunctionConfiguration resource.
type FunctionConfigurationArgs struct {
	ApiId                             pulumi.StringInput
	DataSourceName                    pulumi.StringInput
	Description                       pulumi.StringPtrInput
	FunctionVersion                   pulumi.StringInput
	Name                              pulumi.StringInput
	RequestMappingTemplate            pulumi.StringPtrInput
	RequestMappingTemplateS3Location  pulumi.StringPtrInput
	ResponseMappingTemplate           pulumi.StringPtrInput
	ResponseMappingTemplateS3Location pulumi.StringPtrInput
	SyncConfig                        FunctionConfigurationSyncConfigPtrInput
}

func (FunctionConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*functionConfigurationArgs)(nil)).Elem()
}

type FunctionConfigurationInput interface {
	pulumi.Input

	ToFunctionConfigurationOutput() FunctionConfigurationOutput
	ToFunctionConfigurationOutputWithContext(ctx context.Context) FunctionConfigurationOutput
}

func (*FunctionConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((*FunctionConfiguration)(nil))
}

func (i *FunctionConfiguration) ToFunctionConfigurationOutput() FunctionConfigurationOutput {
	return i.ToFunctionConfigurationOutputWithContext(context.Background())
}

func (i *FunctionConfiguration) ToFunctionConfigurationOutputWithContext(ctx context.Context) FunctionConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FunctionConfigurationOutput)
}

type FunctionConfigurationOutput struct{ *pulumi.OutputState }

func (FunctionConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FunctionConfiguration)(nil))
}

func (o FunctionConfigurationOutput) ToFunctionConfigurationOutput() FunctionConfigurationOutput {
	return o
}

func (o FunctionConfigurationOutput) ToFunctionConfigurationOutputWithContext(ctx context.Context) FunctionConfigurationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(FunctionConfigurationOutput{})
}
