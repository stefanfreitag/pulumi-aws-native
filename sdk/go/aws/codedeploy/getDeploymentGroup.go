// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package codedeploy

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CodeDeploy::DeploymentGroup
func LookupDeploymentGroup(ctx *pulumi.Context, args *LookupDeploymentGroupArgs, opts ...pulumi.InvokeOption) (*LookupDeploymentGroupResult, error) {
	var rv LookupDeploymentGroupResult
	err := ctx.Invoke("aws-native:codedeploy:getDeploymentGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDeploymentGroupArgs struct {
	Id string `pulumi:"id"`
}

type LookupDeploymentGroupResult struct {
	AlarmConfiguration               *DeploymentGroupAlarmConfiguration               `pulumi:"alarmConfiguration"`
	AutoRollbackConfiguration        *DeploymentGroupAutoRollbackConfiguration        `pulumi:"autoRollbackConfiguration"`
	AutoScalingGroups                []string                                         `pulumi:"autoScalingGroups"`
	BlueGreenDeploymentConfiguration *DeploymentGroupBlueGreenDeploymentConfiguration `pulumi:"blueGreenDeploymentConfiguration"`
	Deployment                       *DeploymentGroupDeployment                       `pulumi:"deployment"`
	DeploymentConfigName             *string                                          `pulumi:"deploymentConfigName"`
	DeploymentStyle                  *DeploymentGroupDeploymentStyle                  `pulumi:"deploymentStyle"`
	ECSServices                      []DeploymentGroupECSService                      `pulumi:"eCSServices"`
	Ec2TagFilters                    []DeploymentGroupEC2TagFilter                    `pulumi:"ec2TagFilters"`
	Ec2TagSet                        *DeploymentGroupEC2TagSet                        `pulumi:"ec2TagSet"`
	Id                               *string                                          `pulumi:"id"`
	LoadBalancerInfo                 *DeploymentGroupLoadBalancerInfo                 `pulumi:"loadBalancerInfo"`
	OnPremisesInstanceTagFilters     []DeploymentGroupTagFilter                       `pulumi:"onPremisesInstanceTagFilters"`
	OnPremisesTagSet                 *DeploymentGroupOnPremisesTagSet                 `pulumi:"onPremisesTagSet"`
	OutdatedInstancesStrategy        *string                                          `pulumi:"outdatedInstancesStrategy"`
	ServiceRoleArn                   *string                                          `pulumi:"serviceRoleArn"`
	Tags                             []DeploymentGroupTag                             `pulumi:"tags"`
	TriggerConfigurations            []DeploymentGroupTriggerConfig                   `pulumi:"triggerConfigurations"`
}

func LookupDeploymentGroupOutput(ctx *pulumi.Context, args LookupDeploymentGroupOutputArgs, opts ...pulumi.InvokeOption) LookupDeploymentGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDeploymentGroupResult, error) {
			args := v.(LookupDeploymentGroupArgs)
			r, err := LookupDeploymentGroup(ctx, &args, opts...)
			var s LookupDeploymentGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDeploymentGroupResultOutput)
}

type LookupDeploymentGroupOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupDeploymentGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDeploymentGroupArgs)(nil)).Elem()
}

type LookupDeploymentGroupResultOutput struct{ *pulumi.OutputState }

func (LookupDeploymentGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDeploymentGroupResult)(nil)).Elem()
}

func (o LookupDeploymentGroupResultOutput) ToLookupDeploymentGroupResultOutput() LookupDeploymentGroupResultOutput {
	return o
}

func (o LookupDeploymentGroupResultOutput) ToLookupDeploymentGroupResultOutputWithContext(ctx context.Context) LookupDeploymentGroupResultOutput {
	return o
}

func (o LookupDeploymentGroupResultOutput) AlarmConfiguration() DeploymentGroupAlarmConfigurationPtrOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) *DeploymentGroupAlarmConfiguration { return v.AlarmConfiguration }).(DeploymentGroupAlarmConfigurationPtrOutput)
}

func (o LookupDeploymentGroupResultOutput) AutoRollbackConfiguration() DeploymentGroupAutoRollbackConfigurationPtrOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) *DeploymentGroupAutoRollbackConfiguration {
		return v.AutoRollbackConfiguration
	}).(DeploymentGroupAutoRollbackConfigurationPtrOutput)
}

func (o LookupDeploymentGroupResultOutput) AutoScalingGroups() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) []string { return v.AutoScalingGroups }).(pulumi.StringArrayOutput)
}

func (o LookupDeploymentGroupResultOutput) BlueGreenDeploymentConfiguration() DeploymentGroupBlueGreenDeploymentConfigurationPtrOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) *DeploymentGroupBlueGreenDeploymentConfiguration {
		return v.BlueGreenDeploymentConfiguration
	}).(DeploymentGroupBlueGreenDeploymentConfigurationPtrOutput)
}

func (o LookupDeploymentGroupResultOutput) Deployment() DeploymentGroupDeploymentPtrOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) *DeploymentGroupDeployment { return v.Deployment }).(DeploymentGroupDeploymentPtrOutput)
}

func (o LookupDeploymentGroupResultOutput) DeploymentConfigName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) *string { return v.DeploymentConfigName }).(pulumi.StringPtrOutput)
}

func (o LookupDeploymentGroupResultOutput) DeploymentStyle() DeploymentGroupDeploymentStylePtrOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) *DeploymentGroupDeploymentStyle { return v.DeploymentStyle }).(DeploymentGroupDeploymentStylePtrOutput)
}

func (o LookupDeploymentGroupResultOutput) ECSServices() DeploymentGroupECSServiceArrayOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) []DeploymentGroupECSService { return v.ECSServices }).(DeploymentGroupECSServiceArrayOutput)
}

func (o LookupDeploymentGroupResultOutput) Ec2TagFilters() DeploymentGroupEC2TagFilterArrayOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) []DeploymentGroupEC2TagFilter { return v.Ec2TagFilters }).(DeploymentGroupEC2TagFilterArrayOutput)
}

func (o LookupDeploymentGroupResultOutput) Ec2TagSet() DeploymentGroupEC2TagSetPtrOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) *DeploymentGroupEC2TagSet { return v.Ec2TagSet }).(DeploymentGroupEC2TagSetPtrOutput)
}

func (o LookupDeploymentGroupResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupDeploymentGroupResultOutput) LoadBalancerInfo() DeploymentGroupLoadBalancerInfoPtrOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) *DeploymentGroupLoadBalancerInfo { return v.LoadBalancerInfo }).(DeploymentGroupLoadBalancerInfoPtrOutput)
}

func (o LookupDeploymentGroupResultOutput) OnPremisesInstanceTagFilters() DeploymentGroupTagFilterArrayOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) []DeploymentGroupTagFilter { return v.OnPremisesInstanceTagFilters }).(DeploymentGroupTagFilterArrayOutput)
}

func (o LookupDeploymentGroupResultOutput) OnPremisesTagSet() DeploymentGroupOnPremisesTagSetPtrOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) *DeploymentGroupOnPremisesTagSet { return v.OnPremisesTagSet }).(DeploymentGroupOnPremisesTagSetPtrOutput)
}

func (o LookupDeploymentGroupResultOutput) OutdatedInstancesStrategy() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) *string { return v.OutdatedInstancesStrategy }).(pulumi.StringPtrOutput)
}

func (o LookupDeploymentGroupResultOutput) ServiceRoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) *string { return v.ServiceRoleArn }).(pulumi.StringPtrOutput)
}

func (o LookupDeploymentGroupResultOutput) Tags() DeploymentGroupTagArrayOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) []DeploymentGroupTag { return v.Tags }).(DeploymentGroupTagArrayOutput)
}

func (o LookupDeploymentGroupResultOutput) TriggerConfigurations() DeploymentGroupTriggerConfigArrayOutput {
	return o.ApplyT(func(v LookupDeploymentGroupResult) []DeploymentGroupTriggerConfig { return v.TriggerConfigurations }).(DeploymentGroupTriggerConfigArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDeploymentGroupResultOutput{})
}
