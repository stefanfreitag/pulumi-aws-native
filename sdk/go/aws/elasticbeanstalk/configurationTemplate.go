// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package elasticbeanstalk

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ElasticBeanstalk::ConfigurationTemplate
type ConfigurationTemplate struct {
	pulumi.CustomResourceState

	// The name of the Elastic Beanstalk application to associate with this configuration template.
	ApplicationName pulumi.StringOutput `pulumi:"applicationName"`
	// An optional description for this configuration.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The ID of an environment whose settings you want to use to create the configuration template. You must specify EnvironmentId if you don't specify PlatformArn, SolutionStackName, or SourceConfiguration.
	EnvironmentId pulumi.StringPtrOutput `pulumi:"environmentId"`
	// Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see [Option Values](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the AWS Elastic Beanstalk Developer Guide.
	OptionSettings ConfigurationTemplateConfigurationOptionSettingArrayOutput `pulumi:"optionSettings"`
	// The Amazon Resource Name (ARN) of the custom platform. For more information, see [Custom Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html) in the AWS Elastic Beanstalk Developer Guide.
	PlatformArn pulumi.StringPtrOutput `pulumi:"platformArn"`
	// The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, 64bit Amazon Linux 2013.09 running Tomcat 7 Java 7. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see [Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html) in the AWS Elastic Beanstalk Developer Guide.
	//
	//  You must specify SolutionStackName if you don't specify PlatformArn, EnvironmentId, or SourceConfiguration.
	//
	//  Use the ListAvailableSolutionStacks API to obtain a list of available solution stacks.
	SolutionStackName pulumi.StringPtrOutput `pulumi:"solutionStackName"`
	// An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.
	//
	// Values specified in OptionSettings override any values obtained from the SourceConfiguration.
	//
	// You must specify SourceConfiguration if you don't specify PlatformArn, EnvironmentId, or SolutionStackName.
	//
	// Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.
	SourceConfiguration ConfigurationTemplateSourceConfigurationPtrOutput `pulumi:"sourceConfiguration"`
	// The name of the configuration template
	TemplateName pulumi.StringOutput `pulumi:"templateName"`
}

// NewConfigurationTemplate registers a new resource with the given unique name, arguments, and options.
func NewConfigurationTemplate(ctx *pulumi.Context,
	name string, args *ConfigurationTemplateArgs, opts ...pulumi.ResourceOption) (*ConfigurationTemplate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApplicationName == nil {
		return nil, errors.New("invalid value for required argument 'ApplicationName'")
	}
	var resource ConfigurationTemplate
	err := ctx.RegisterResource("aws-native:elasticbeanstalk:ConfigurationTemplate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConfigurationTemplate gets an existing ConfigurationTemplate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConfigurationTemplate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConfigurationTemplateState, opts ...pulumi.ResourceOption) (*ConfigurationTemplate, error) {
	var resource ConfigurationTemplate
	err := ctx.ReadResource("aws-native:elasticbeanstalk:ConfigurationTemplate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ConfigurationTemplate resources.
type configurationTemplateState struct {
}

type ConfigurationTemplateState struct {
}

func (ConfigurationTemplateState) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationTemplateState)(nil)).Elem()
}

type configurationTemplateArgs struct {
	// The name of the Elastic Beanstalk application to associate with this configuration template.
	ApplicationName string `pulumi:"applicationName"`
	// An optional description for this configuration.
	Description *string `pulumi:"description"`
	// The ID of an environment whose settings you want to use to create the configuration template. You must specify EnvironmentId if you don't specify PlatformArn, SolutionStackName, or SourceConfiguration.
	EnvironmentId *string `pulumi:"environmentId"`
	// Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see [Option Values](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the AWS Elastic Beanstalk Developer Guide.
	OptionSettings []ConfigurationTemplateConfigurationOptionSetting `pulumi:"optionSettings"`
	// The Amazon Resource Name (ARN) of the custom platform. For more information, see [Custom Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html) in the AWS Elastic Beanstalk Developer Guide.
	PlatformArn *string `pulumi:"platformArn"`
	// The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, 64bit Amazon Linux 2013.09 running Tomcat 7 Java 7. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see [Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html) in the AWS Elastic Beanstalk Developer Guide.
	//
	//  You must specify SolutionStackName if you don't specify PlatformArn, EnvironmentId, or SourceConfiguration.
	//
	//  Use the ListAvailableSolutionStacks API to obtain a list of available solution stacks.
	SolutionStackName *string `pulumi:"solutionStackName"`
	// An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.
	//
	// Values specified in OptionSettings override any values obtained from the SourceConfiguration.
	//
	// You must specify SourceConfiguration if you don't specify PlatformArn, EnvironmentId, or SolutionStackName.
	//
	// Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.
	SourceConfiguration *ConfigurationTemplateSourceConfiguration `pulumi:"sourceConfiguration"`
}

// The set of arguments for constructing a ConfigurationTemplate resource.
type ConfigurationTemplateArgs struct {
	// The name of the Elastic Beanstalk application to associate with this configuration template.
	ApplicationName pulumi.StringInput
	// An optional description for this configuration.
	Description pulumi.StringPtrInput
	// The ID of an environment whose settings you want to use to create the configuration template. You must specify EnvironmentId if you don't specify PlatformArn, SolutionStackName, or SourceConfiguration.
	EnvironmentId pulumi.StringPtrInput
	// Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see [Option Values](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the AWS Elastic Beanstalk Developer Guide.
	OptionSettings ConfigurationTemplateConfigurationOptionSettingArrayInput
	// The Amazon Resource Name (ARN) of the custom platform. For more information, see [Custom Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html) in the AWS Elastic Beanstalk Developer Guide.
	PlatformArn pulumi.StringPtrInput
	// The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, 64bit Amazon Linux 2013.09 running Tomcat 7 Java 7. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see [Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html) in the AWS Elastic Beanstalk Developer Guide.
	//
	//  You must specify SolutionStackName if you don't specify PlatformArn, EnvironmentId, or SourceConfiguration.
	//
	//  Use the ListAvailableSolutionStacks API to obtain a list of available solution stacks.
	SolutionStackName pulumi.StringPtrInput
	// An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.
	//
	// Values specified in OptionSettings override any values obtained from the SourceConfiguration.
	//
	// You must specify SourceConfiguration if you don't specify PlatformArn, EnvironmentId, or SolutionStackName.
	//
	// Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.
	SourceConfiguration ConfigurationTemplateSourceConfigurationPtrInput
}

func (ConfigurationTemplateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationTemplateArgs)(nil)).Elem()
}

type ConfigurationTemplateInput interface {
	pulumi.Input

	ToConfigurationTemplateOutput() ConfigurationTemplateOutput
	ToConfigurationTemplateOutputWithContext(ctx context.Context) ConfigurationTemplateOutput
}

func (*ConfigurationTemplate) ElementType() reflect.Type {
	return reflect.TypeOf((**ConfigurationTemplate)(nil)).Elem()
}

func (i *ConfigurationTemplate) ToConfigurationTemplateOutput() ConfigurationTemplateOutput {
	return i.ToConfigurationTemplateOutputWithContext(context.Background())
}

func (i *ConfigurationTemplate) ToConfigurationTemplateOutputWithContext(ctx context.Context) ConfigurationTemplateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigurationTemplateOutput)
}

type ConfigurationTemplateOutput struct{ *pulumi.OutputState }

func (ConfigurationTemplateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ConfigurationTemplate)(nil)).Elem()
}

func (o ConfigurationTemplateOutput) ToConfigurationTemplateOutput() ConfigurationTemplateOutput {
	return o
}

func (o ConfigurationTemplateOutput) ToConfigurationTemplateOutputWithContext(ctx context.Context) ConfigurationTemplateOutput {
	return o
}

// The name of the Elastic Beanstalk application to associate with this configuration template.
func (o ConfigurationTemplateOutput) ApplicationName() pulumi.StringOutput {
	return o.ApplyT(func(v *ConfigurationTemplate) pulumi.StringOutput { return v.ApplicationName }).(pulumi.StringOutput)
}

// An optional description for this configuration.
func (o ConfigurationTemplateOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ConfigurationTemplate) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The ID of an environment whose settings you want to use to create the configuration template. You must specify EnvironmentId if you don't specify PlatformArn, SolutionStackName, or SourceConfiguration.
func (o ConfigurationTemplateOutput) EnvironmentId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ConfigurationTemplate) pulumi.StringPtrOutput { return v.EnvironmentId }).(pulumi.StringPtrOutput)
}

// Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see [Option Values](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the AWS Elastic Beanstalk Developer Guide.
func (o ConfigurationTemplateOutput) OptionSettings() ConfigurationTemplateConfigurationOptionSettingArrayOutput {
	return o.ApplyT(func(v *ConfigurationTemplate) ConfigurationTemplateConfigurationOptionSettingArrayOutput {
		return v.OptionSettings
	}).(ConfigurationTemplateConfigurationOptionSettingArrayOutput)
}

// The Amazon Resource Name (ARN) of the custom platform. For more information, see [Custom Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html) in the AWS Elastic Beanstalk Developer Guide.
func (o ConfigurationTemplateOutput) PlatformArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ConfigurationTemplate) pulumi.StringPtrOutput { return v.PlatformArn }).(pulumi.StringPtrOutput)
}

// The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, 64bit Amazon Linux 2013.09 running Tomcat 7 Java 7. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see [Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html) in the AWS Elastic Beanstalk Developer Guide.
//
//	You must specify SolutionStackName if you don't specify PlatformArn, EnvironmentId, or SourceConfiguration.
//
//	Use the ListAvailableSolutionStacks API to obtain a list of available solution stacks.
func (o ConfigurationTemplateOutput) SolutionStackName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ConfigurationTemplate) pulumi.StringPtrOutput { return v.SolutionStackName }).(pulumi.StringPtrOutput)
}

// An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.
//
// Values specified in OptionSettings override any values obtained from the SourceConfiguration.
//
// You must specify SourceConfiguration if you don't specify PlatformArn, EnvironmentId, or SolutionStackName.
//
// Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.
func (o ConfigurationTemplateOutput) SourceConfiguration() ConfigurationTemplateSourceConfigurationPtrOutput {
	return o.ApplyT(func(v *ConfigurationTemplate) ConfigurationTemplateSourceConfigurationPtrOutput {
		return v.SourceConfiguration
	}).(ConfigurationTemplateSourceConfigurationPtrOutput)
}

// The name of the configuration template
func (o ConfigurationTemplateOutput) TemplateName() pulumi.StringOutput {
	return o.ApplyT(func(v *ConfigurationTemplate) pulumi.StringOutput { return v.TemplateName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigurationTemplateInput)(nil)).Elem(), &ConfigurationTemplate{})
	pulumi.RegisterOutputType(ConfigurationTemplateOutput{})
}
