// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package greengrass

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Greengrass::LoggerDefinition
//
// Deprecated: LoggerDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type LoggerDefinition struct {
	pulumi.CustomResourceState

	Arn              pulumi.StringOutput                  `pulumi:"arn"`
	InitialVersion   LoggerDefinitionVersionTypePtrOutput `pulumi:"initialVersion"`
	LatestVersionArn pulumi.StringOutput                  `pulumi:"latestVersionArn"`
	Name             pulumi.StringOutput                  `pulumi:"name"`
	Tags             pulumi.AnyOutput                     `pulumi:"tags"`
}

// NewLoggerDefinition registers a new resource with the given unique name, arguments, and options.
func NewLoggerDefinition(ctx *pulumi.Context,
	name string, args *LoggerDefinitionArgs, opts ...pulumi.ResourceOption) (*LoggerDefinition, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource LoggerDefinition
	err := ctx.RegisterResource("aws-native:greengrass:LoggerDefinition", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLoggerDefinition gets an existing LoggerDefinition resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLoggerDefinition(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LoggerDefinitionState, opts ...pulumi.ResourceOption) (*LoggerDefinition, error) {
	var resource LoggerDefinition
	err := ctx.ReadResource("aws-native:greengrass:LoggerDefinition", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LoggerDefinition resources.
type loggerDefinitionState struct {
}

type LoggerDefinitionState struct {
}

func (LoggerDefinitionState) ElementType() reflect.Type {
	return reflect.TypeOf((*loggerDefinitionState)(nil)).Elem()
}

type loggerDefinitionArgs struct {
	InitialVersion *LoggerDefinitionVersionType `pulumi:"initialVersion"`
	Name           string                       `pulumi:"name"`
	Tags           interface{}                  `pulumi:"tags"`
}

// The set of arguments for constructing a LoggerDefinition resource.
type LoggerDefinitionArgs struct {
	InitialVersion LoggerDefinitionVersionTypePtrInput
	Name           pulumi.StringInput
	Tags           pulumi.Input
}

func (LoggerDefinitionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*loggerDefinitionArgs)(nil)).Elem()
}

type LoggerDefinitionInput interface {
	pulumi.Input

	ToLoggerDefinitionOutput() LoggerDefinitionOutput
	ToLoggerDefinitionOutputWithContext(ctx context.Context) LoggerDefinitionOutput
}

func (*LoggerDefinition) ElementType() reflect.Type {
	return reflect.TypeOf((*LoggerDefinition)(nil))
}

func (i *LoggerDefinition) ToLoggerDefinitionOutput() LoggerDefinitionOutput {
	return i.ToLoggerDefinitionOutputWithContext(context.Background())
}

func (i *LoggerDefinition) ToLoggerDefinitionOutputWithContext(ctx context.Context) LoggerDefinitionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LoggerDefinitionOutput)
}

type LoggerDefinitionOutput struct{ *pulumi.OutputState }

func (LoggerDefinitionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LoggerDefinition)(nil))
}

func (o LoggerDefinitionOutput) ToLoggerDefinitionOutput() LoggerDefinitionOutput {
	return o
}

func (o LoggerDefinitionOutput) ToLoggerDefinitionOutputWithContext(ctx context.Context) LoggerDefinitionOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LoggerDefinitionInput)(nil)).Elem(), &LoggerDefinition{})
	pulumi.RegisterOutputType(LoggerDefinitionOutput{})
}
