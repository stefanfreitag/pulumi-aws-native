// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package redshift

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html
type ClusterLoggingProperties struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-bucketname
	BucketName string `pulumi:"bucketName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-s3keyprefix
	S3KeyPrefix *string `pulumi:"s3KeyPrefix"`
}

// ClusterLoggingPropertiesInput is an input type that accepts ClusterLoggingPropertiesArgs and ClusterLoggingPropertiesOutput values.
// You can construct a concrete instance of `ClusterLoggingPropertiesInput` via:
//
//          ClusterLoggingPropertiesArgs{...}
type ClusterLoggingPropertiesInput interface {
	pulumi.Input

	ToClusterLoggingPropertiesOutput() ClusterLoggingPropertiesOutput
	ToClusterLoggingPropertiesOutputWithContext(context.Context) ClusterLoggingPropertiesOutput
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html
type ClusterLoggingPropertiesArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-bucketname
	BucketName pulumi.StringInput `pulumi:"bucketName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-s3keyprefix
	S3KeyPrefix pulumi.StringPtrInput `pulumi:"s3KeyPrefix"`
}

func (ClusterLoggingPropertiesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ClusterLoggingProperties)(nil)).Elem()
}

func (i ClusterLoggingPropertiesArgs) ToClusterLoggingPropertiesOutput() ClusterLoggingPropertiesOutput {
	return i.ToClusterLoggingPropertiesOutputWithContext(context.Background())
}

func (i ClusterLoggingPropertiesArgs) ToClusterLoggingPropertiesOutputWithContext(ctx context.Context) ClusterLoggingPropertiesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterLoggingPropertiesOutput)
}

func (i ClusterLoggingPropertiesArgs) ToClusterLoggingPropertiesPtrOutput() ClusterLoggingPropertiesPtrOutput {
	return i.ToClusterLoggingPropertiesPtrOutputWithContext(context.Background())
}

func (i ClusterLoggingPropertiesArgs) ToClusterLoggingPropertiesPtrOutputWithContext(ctx context.Context) ClusterLoggingPropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterLoggingPropertiesOutput).ToClusterLoggingPropertiesPtrOutputWithContext(ctx)
}

// ClusterLoggingPropertiesPtrInput is an input type that accepts ClusterLoggingPropertiesArgs, ClusterLoggingPropertiesPtr and ClusterLoggingPropertiesPtrOutput values.
// You can construct a concrete instance of `ClusterLoggingPropertiesPtrInput` via:
//
//          ClusterLoggingPropertiesArgs{...}
//
//  or:
//
//          nil
type ClusterLoggingPropertiesPtrInput interface {
	pulumi.Input

	ToClusterLoggingPropertiesPtrOutput() ClusterLoggingPropertiesPtrOutput
	ToClusterLoggingPropertiesPtrOutputWithContext(context.Context) ClusterLoggingPropertiesPtrOutput
}

type clusterLoggingPropertiesPtrType ClusterLoggingPropertiesArgs

func ClusterLoggingPropertiesPtr(v *ClusterLoggingPropertiesArgs) ClusterLoggingPropertiesPtrInput {
	return (*clusterLoggingPropertiesPtrType)(v)
}

func (*clusterLoggingPropertiesPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ClusterLoggingProperties)(nil)).Elem()
}

func (i *clusterLoggingPropertiesPtrType) ToClusterLoggingPropertiesPtrOutput() ClusterLoggingPropertiesPtrOutput {
	return i.ToClusterLoggingPropertiesPtrOutputWithContext(context.Background())
}

func (i *clusterLoggingPropertiesPtrType) ToClusterLoggingPropertiesPtrOutputWithContext(ctx context.Context) ClusterLoggingPropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterLoggingPropertiesPtrOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html
type ClusterLoggingPropertiesOutput struct{ *pulumi.OutputState }

func (ClusterLoggingPropertiesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ClusterLoggingProperties)(nil)).Elem()
}

func (o ClusterLoggingPropertiesOutput) ToClusterLoggingPropertiesOutput() ClusterLoggingPropertiesOutput {
	return o
}

func (o ClusterLoggingPropertiesOutput) ToClusterLoggingPropertiesOutputWithContext(ctx context.Context) ClusterLoggingPropertiesOutput {
	return o
}

func (o ClusterLoggingPropertiesOutput) ToClusterLoggingPropertiesPtrOutput() ClusterLoggingPropertiesPtrOutput {
	return o.ToClusterLoggingPropertiesPtrOutputWithContext(context.Background())
}

func (o ClusterLoggingPropertiesOutput) ToClusterLoggingPropertiesPtrOutputWithContext(ctx context.Context) ClusterLoggingPropertiesPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ClusterLoggingProperties) *ClusterLoggingProperties {
		return &v
	}).(ClusterLoggingPropertiesPtrOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-bucketname
func (o ClusterLoggingPropertiesOutput) BucketName() pulumi.StringOutput {
	return o.ApplyT(func(v ClusterLoggingProperties) string { return v.BucketName }).(pulumi.StringOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-s3keyprefix
func (o ClusterLoggingPropertiesOutput) S3KeyPrefix() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ClusterLoggingProperties) *string { return v.S3KeyPrefix }).(pulumi.StringPtrOutput)
}

type ClusterLoggingPropertiesPtrOutput struct{ *pulumi.OutputState }

func (ClusterLoggingPropertiesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ClusterLoggingProperties)(nil)).Elem()
}

func (o ClusterLoggingPropertiesPtrOutput) ToClusterLoggingPropertiesPtrOutput() ClusterLoggingPropertiesPtrOutput {
	return o
}

func (o ClusterLoggingPropertiesPtrOutput) ToClusterLoggingPropertiesPtrOutputWithContext(ctx context.Context) ClusterLoggingPropertiesPtrOutput {
	return o
}

func (o ClusterLoggingPropertiesPtrOutput) Elem() ClusterLoggingPropertiesOutput {
	return o.ApplyT(func(v *ClusterLoggingProperties) ClusterLoggingProperties {
		if v != nil {
			return *v
		}
		var ret ClusterLoggingProperties
		return ret
	}).(ClusterLoggingPropertiesOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-bucketname
func (o ClusterLoggingPropertiesPtrOutput) BucketName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ClusterLoggingProperties) *string {
		if v == nil {
			return nil
		}
		return &v.BucketName
	}).(pulumi.StringPtrOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-s3keyprefix
func (o ClusterLoggingPropertiesPtrOutput) S3KeyPrefix() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ClusterLoggingProperties) *string {
		if v == nil {
			return nil
		}
		return v.S3KeyPrefix
	}).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(ClusterLoggingPropertiesOutput{})
	pulumi.RegisterOutputType(ClusterLoggingPropertiesPtrOutput{})
}
