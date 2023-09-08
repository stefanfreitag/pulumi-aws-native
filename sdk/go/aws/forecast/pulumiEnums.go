// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package forecast

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Data type of the field
type DatasetAttributesItemPropertiesAttributeType string

const (
	DatasetAttributesItemPropertiesAttributeTypeString      = DatasetAttributesItemPropertiesAttributeType("string")
	DatasetAttributesItemPropertiesAttributeTypeInteger     = DatasetAttributesItemPropertiesAttributeType("integer")
	DatasetAttributesItemPropertiesAttributeTypeFloat       = DatasetAttributesItemPropertiesAttributeType("float")
	DatasetAttributesItemPropertiesAttributeTypeTimestamp   = DatasetAttributesItemPropertiesAttributeType("timestamp")
	DatasetAttributesItemPropertiesAttributeTypeGeolocation = DatasetAttributesItemPropertiesAttributeType("geolocation")
)

func (DatasetAttributesItemPropertiesAttributeType) ElementType() reflect.Type {
	return reflect.TypeOf((*DatasetAttributesItemPropertiesAttributeType)(nil)).Elem()
}

func (e DatasetAttributesItemPropertiesAttributeType) ToDatasetAttributesItemPropertiesAttributeTypeOutput() DatasetAttributesItemPropertiesAttributeTypeOutput {
	return pulumi.ToOutput(e).(DatasetAttributesItemPropertiesAttributeTypeOutput)
}

func (e DatasetAttributesItemPropertiesAttributeType) ToDatasetAttributesItemPropertiesAttributeTypeOutputWithContext(ctx context.Context) DatasetAttributesItemPropertiesAttributeTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(DatasetAttributesItemPropertiesAttributeTypeOutput)
}

func (e DatasetAttributesItemPropertiesAttributeType) ToDatasetAttributesItemPropertiesAttributeTypePtrOutput() DatasetAttributesItemPropertiesAttributeTypePtrOutput {
	return e.ToDatasetAttributesItemPropertiesAttributeTypePtrOutputWithContext(context.Background())
}

func (e DatasetAttributesItemPropertiesAttributeType) ToDatasetAttributesItemPropertiesAttributeTypePtrOutputWithContext(ctx context.Context) DatasetAttributesItemPropertiesAttributeTypePtrOutput {
	return DatasetAttributesItemPropertiesAttributeType(e).ToDatasetAttributesItemPropertiesAttributeTypeOutputWithContext(ctx).ToDatasetAttributesItemPropertiesAttributeTypePtrOutputWithContext(ctx)
}

func (e DatasetAttributesItemPropertiesAttributeType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e DatasetAttributesItemPropertiesAttributeType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e DatasetAttributesItemPropertiesAttributeType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e DatasetAttributesItemPropertiesAttributeType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type DatasetAttributesItemPropertiesAttributeTypeOutput struct{ *pulumi.OutputState }

func (DatasetAttributesItemPropertiesAttributeTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DatasetAttributesItemPropertiesAttributeType)(nil)).Elem()
}

func (o DatasetAttributesItemPropertiesAttributeTypeOutput) ToDatasetAttributesItemPropertiesAttributeTypeOutput() DatasetAttributesItemPropertiesAttributeTypeOutput {
	return o
}

func (o DatasetAttributesItemPropertiesAttributeTypeOutput) ToDatasetAttributesItemPropertiesAttributeTypeOutputWithContext(ctx context.Context) DatasetAttributesItemPropertiesAttributeTypeOutput {
	return o
}

func (o DatasetAttributesItemPropertiesAttributeTypeOutput) ToDatasetAttributesItemPropertiesAttributeTypePtrOutput() DatasetAttributesItemPropertiesAttributeTypePtrOutput {
	return o.ToDatasetAttributesItemPropertiesAttributeTypePtrOutputWithContext(context.Background())
}

func (o DatasetAttributesItemPropertiesAttributeTypeOutput) ToDatasetAttributesItemPropertiesAttributeTypePtrOutputWithContext(ctx context.Context) DatasetAttributesItemPropertiesAttributeTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DatasetAttributesItemPropertiesAttributeType) *DatasetAttributesItemPropertiesAttributeType {
		return &v
	}).(DatasetAttributesItemPropertiesAttributeTypePtrOutput)
}

func (o DatasetAttributesItemPropertiesAttributeTypeOutput) ToOutput(ctx context.Context) pulumix.Output[DatasetAttributesItemPropertiesAttributeType] {
	return pulumix.Output[DatasetAttributesItemPropertiesAttributeType]{
		OutputState: o.OutputState,
	}
}

func (o DatasetAttributesItemPropertiesAttributeTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o DatasetAttributesItemPropertiesAttributeTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DatasetAttributesItemPropertiesAttributeType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o DatasetAttributesItemPropertiesAttributeTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DatasetAttributesItemPropertiesAttributeTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DatasetAttributesItemPropertiesAttributeType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type DatasetAttributesItemPropertiesAttributeTypePtrOutput struct{ *pulumi.OutputState }

func (DatasetAttributesItemPropertiesAttributeTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DatasetAttributesItemPropertiesAttributeType)(nil)).Elem()
}

func (o DatasetAttributesItemPropertiesAttributeTypePtrOutput) ToDatasetAttributesItemPropertiesAttributeTypePtrOutput() DatasetAttributesItemPropertiesAttributeTypePtrOutput {
	return o
}

func (o DatasetAttributesItemPropertiesAttributeTypePtrOutput) ToDatasetAttributesItemPropertiesAttributeTypePtrOutputWithContext(ctx context.Context) DatasetAttributesItemPropertiesAttributeTypePtrOutput {
	return o
}

func (o DatasetAttributesItemPropertiesAttributeTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*DatasetAttributesItemPropertiesAttributeType] {
	return pulumix.Output[*DatasetAttributesItemPropertiesAttributeType]{
		OutputState: o.OutputState,
	}
}

func (o DatasetAttributesItemPropertiesAttributeTypePtrOutput) Elem() DatasetAttributesItemPropertiesAttributeTypeOutput {
	return o.ApplyT(func(v *DatasetAttributesItemPropertiesAttributeType) DatasetAttributesItemPropertiesAttributeType {
		if v != nil {
			return *v
		}
		var ret DatasetAttributesItemPropertiesAttributeType
		return ret
	}).(DatasetAttributesItemPropertiesAttributeTypeOutput)
}

func (o DatasetAttributesItemPropertiesAttributeTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DatasetAttributesItemPropertiesAttributeTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *DatasetAttributesItemPropertiesAttributeType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// DatasetAttributesItemPropertiesAttributeTypeInput is an input type that accepts DatasetAttributesItemPropertiesAttributeTypeArgs and DatasetAttributesItemPropertiesAttributeTypeOutput values.
// You can construct a concrete instance of `DatasetAttributesItemPropertiesAttributeTypeInput` via:
//
//	DatasetAttributesItemPropertiesAttributeTypeArgs{...}
type DatasetAttributesItemPropertiesAttributeTypeInput interface {
	pulumi.Input

	ToDatasetAttributesItemPropertiesAttributeTypeOutput() DatasetAttributesItemPropertiesAttributeTypeOutput
	ToDatasetAttributesItemPropertiesAttributeTypeOutputWithContext(context.Context) DatasetAttributesItemPropertiesAttributeTypeOutput
}

var datasetAttributesItemPropertiesAttributeTypePtrType = reflect.TypeOf((**DatasetAttributesItemPropertiesAttributeType)(nil)).Elem()

type DatasetAttributesItemPropertiesAttributeTypePtrInput interface {
	pulumi.Input

	ToDatasetAttributesItemPropertiesAttributeTypePtrOutput() DatasetAttributesItemPropertiesAttributeTypePtrOutput
	ToDatasetAttributesItemPropertiesAttributeTypePtrOutputWithContext(context.Context) DatasetAttributesItemPropertiesAttributeTypePtrOutput
}

type datasetAttributesItemPropertiesAttributeTypePtr string

func DatasetAttributesItemPropertiesAttributeTypePtr(v string) DatasetAttributesItemPropertiesAttributeTypePtrInput {
	return (*datasetAttributesItemPropertiesAttributeTypePtr)(&v)
}

func (*datasetAttributesItemPropertiesAttributeTypePtr) ElementType() reflect.Type {
	return datasetAttributesItemPropertiesAttributeTypePtrType
}

func (in *datasetAttributesItemPropertiesAttributeTypePtr) ToDatasetAttributesItemPropertiesAttributeTypePtrOutput() DatasetAttributesItemPropertiesAttributeTypePtrOutput {
	return pulumi.ToOutput(in).(DatasetAttributesItemPropertiesAttributeTypePtrOutput)
}

func (in *datasetAttributesItemPropertiesAttributeTypePtr) ToDatasetAttributesItemPropertiesAttributeTypePtrOutputWithContext(ctx context.Context) DatasetAttributesItemPropertiesAttributeTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(DatasetAttributesItemPropertiesAttributeTypePtrOutput)
}

func (in *datasetAttributesItemPropertiesAttributeTypePtr) ToOutput(ctx context.Context) pulumix.Output[*DatasetAttributesItemPropertiesAttributeType] {
	return pulumix.Output[*DatasetAttributesItemPropertiesAttributeType]{
		OutputState: in.ToDatasetAttributesItemPropertiesAttributeTypePtrOutputWithContext(ctx).OutputState,
	}
}

// The domain associated with the dataset
type DatasetDomain string

const (
	DatasetDomainRetail            = DatasetDomain("RETAIL")
	DatasetDomainCustom            = DatasetDomain("CUSTOM")
	DatasetDomainInventoryPlanning = DatasetDomain("INVENTORY_PLANNING")
	DatasetDomainEc2Capacity       = DatasetDomain("EC2_CAPACITY")
	DatasetDomainWorkForce         = DatasetDomain("WORK_FORCE")
	DatasetDomainWebTraffic        = DatasetDomain("WEB_TRAFFIC")
	DatasetDomainMetrics           = DatasetDomain("METRICS")
)

func (DatasetDomain) ElementType() reflect.Type {
	return reflect.TypeOf((*DatasetDomain)(nil)).Elem()
}

func (e DatasetDomain) ToDatasetDomainOutput() DatasetDomainOutput {
	return pulumi.ToOutput(e).(DatasetDomainOutput)
}

func (e DatasetDomain) ToDatasetDomainOutputWithContext(ctx context.Context) DatasetDomainOutput {
	return pulumi.ToOutputWithContext(ctx, e).(DatasetDomainOutput)
}

func (e DatasetDomain) ToDatasetDomainPtrOutput() DatasetDomainPtrOutput {
	return e.ToDatasetDomainPtrOutputWithContext(context.Background())
}

func (e DatasetDomain) ToDatasetDomainPtrOutputWithContext(ctx context.Context) DatasetDomainPtrOutput {
	return DatasetDomain(e).ToDatasetDomainOutputWithContext(ctx).ToDatasetDomainPtrOutputWithContext(ctx)
}

func (e DatasetDomain) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e DatasetDomain) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e DatasetDomain) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e DatasetDomain) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type DatasetDomainOutput struct{ *pulumi.OutputState }

func (DatasetDomainOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DatasetDomain)(nil)).Elem()
}

func (o DatasetDomainOutput) ToDatasetDomainOutput() DatasetDomainOutput {
	return o
}

func (o DatasetDomainOutput) ToDatasetDomainOutputWithContext(ctx context.Context) DatasetDomainOutput {
	return o
}

func (o DatasetDomainOutput) ToDatasetDomainPtrOutput() DatasetDomainPtrOutput {
	return o.ToDatasetDomainPtrOutputWithContext(context.Background())
}

func (o DatasetDomainOutput) ToDatasetDomainPtrOutputWithContext(ctx context.Context) DatasetDomainPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DatasetDomain) *DatasetDomain {
		return &v
	}).(DatasetDomainPtrOutput)
}

func (o DatasetDomainOutput) ToOutput(ctx context.Context) pulumix.Output[DatasetDomain] {
	return pulumix.Output[DatasetDomain]{
		OutputState: o.OutputState,
	}
}

func (o DatasetDomainOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o DatasetDomainOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DatasetDomain) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o DatasetDomainOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DatasetDomainOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DatasetDomain) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type DatasetDomainPtrOutput struct{ *pulumi.OutputState }

func (DatasetDomainPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DatasetDomain)(nil)).Elem()
}

func (o DatasetDomainPtrOutput) ToDatasetDomainPtrOutput() DatasetDomainPtrOutput {
	return o
}

func (o DatasetDomainPtrOutput) ToDatasetDomainPtrOutputWithContext(ctx context.Context) DatasetDomainPtrOutput {
	return o
}

func (o DatasetDomainPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*DatasetDomain] {
	return pulumix.Output[*DatasetDomain]{
		OutputState: o.OutputState,
	}
}

func (o DatasetDomainPtrOutput) Elem() DatasetDomainOutput {
	return o.ApplyT(func(v *DatasetDomain) DatasetDomain {
		if v != nil {
			return *v
		}
		var ret DatasetDomain
		return ret
	}).(DatasetDomainOutput)
}

func (o DatasetDomainPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DatasetDomainPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *DatasetDomain) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// DatasetDomainInput is an input type that accepts DatasetDomainArgs and DatasetDomainOutput values.
// You can construct a concrete instance of `DatasetDomainInput` via:
//
//	DatasetDomainArgs{...}
type DatasetDomainInput interface {
	pulumi.Input

	ToDatasetDomainOutput() DatasetDomainOutput
	ToDatasetDomainOutputWithContext(context.Context) DatasetDomainOutput
}

var datasetDomainPtrType = reflect.TypeOf((**DatasetDomain)(nil)).Elem()

type DatasetDomainPtrInput interface {
	pulumi.Input

	ToDatasetDomainPtrOutput() DatasetDomainPtrOutput
	ToDatasetDomainPtrOutputWithContext(context.Context) DatasetDomainPtrOutput
}

type datasetDomainPtr string

func DatasetDomainPtr(v string) DatasetDomainPtrInput {
	return (*datasetDomainPtr)(&v)
}

func (*datasetDomainPtr) ElementType() reflect.Type {
	return datasetDomainPtrType
}

func (in *datasetDomainPtr) ToDatasetDomainPtrOutput() DatasetDomainPtrOutput {
	return pulumi.ToOutput(in).(DatasetDomainPtrOutput)
}

func (in *datasetDomainPtr) ToDatasetDomainPtrOutputWithContext(ctx context.Context) DatasetDomainPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(DatasetDomainPtrOutput)
}

func (in *datasetDomainPtr) ToOutput(ctx context.Context) pulumix.Output[*DatasetDomain] {
	return pulumix.Output[*DatasetDomain]{
		OutputState: in.ToDatasetDomainPtrOutputWithContext(ctx).OutputState,
	}
}

// The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the Domain parameter of the CreateDataset operation must match.
type DatasetGroupDomain string

const (
	DatasetGroupDomainRetail            = DatasetGroupDomain("RETAIL")
	DatasetGroupDomainCustom            = DatasetGroupDomain("CUSTOM")
	DatasetGroupDomainInventoryPlanning = DatasetGroupDomain("INVENTORY_PLANNING")
	DatasetGroupDomainEc2Capacity       = DatasetGroupDomain("EC2_CAPACITY")
	DatasetGroupDomainWorkForce         = DatasetGroupDomain("WORK_FORCE")
	DatasetGroupDomainWebTraffic        = DatasetGroupDomain("WEB_TRAFFIC")
	DatasetGroupDomainMetrics           = DatasetGroupDomain("METRICS")
)

func (DatasetGroupDomain) ElementType() reflect.Type {
	return reflect.TypeOf((*DatasetGroupDomain)(nil)).Elem()
}

func (e DatasetGroupDomain) ToDatasetGroupDomainOutput() DatasetGroupDomainOutput {
	return pulumi.ToOutput(e).(DatasetGroupDomainOutput)
}

func (e DatasetGroupDomain) ToDatasetGroupDomainOutputWithContext(ctx context.Context) DatasetGroupDomainOutput {
	return pulumi.ToOutputWithContext(ctx, e).(DatasetGroupDomainOutput)
}

func (e DatasetGroupDomain) ToDatasetGroupDomainPtrOutput() DatasetGroupDomainPtrOutput {
	return e.ToDatasetGroupDomainPtrOutputWithContext(context.Background())
}

func (e DatasetGroupDomain) ToDatasetGroupDomainPtrOutputWithContext(ctx context.Context) DatasetGroupDomainPtrOutput {
	return DatasetGroupDomain(e).ToDatasetGroupDomainOutputWithContext(ctx).ToDatasetGroupDomainPtrOutputWithContext(ctx)
}

func (e DatasetGroupDomain) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e DatasetGroupDomain) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e DatasetGroupDomain) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e DatasetGroupDomain) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type DatasetGroupDomainOutput struct{ *pulumi.OutputState }

func (DatasetGroupDomainOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DatasetGroupDomain)(nil)).Elem()
}

func (o DatasetGroupDomainOutput) ToDatasetGroupDomainOutput() DatasetGroupDomainOutput {
	return o
}

func (o DatasetGroupDomainOutput) ToDatasetGroupDomainOutputWithContext(ctx context.Context) DatasetGroupDomainOutput {
	return o
}

func (o DatasetGroupDomainOutput) ToDatasetGroupDomainPtrOutput() DatasetGroupDomainPtrOutput {
	return o.ToDatasetGroupDomainPtrOutputWithContext(context.Background())
}

func (o DatasetGroupDomainOutput) ToDatasetGroupDomainPtrOutputWithContext(ctx context.Context) DatasetGroupDomainPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DatasetGroupDomain) *DatasetGroupDomain {
		return &v
	}).(DatasetGroupDomainPtrOutput)
}

func (o DatasetGroupDomainOutput) ToOutput(ctx context.Context) pulumix.Output[DatasetGroupDomain] {
	return pulumix.Output[DatasetGroupDomain]{
		OutputState: o.OutputState,
	}
}

func (o DatasetGroupDomainOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o DatasetGroupDomainOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DatasetGroupDomain) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o DatasetGroupDomainOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DatasetGroupDomainOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DatasetGroupDomain) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type DatasetGroupDomainPtrOutput struct{ *pulumi.OutputState }

func (DatasetGroupDomainPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DatasetGroupDomain)(nil)).Elem()
}

func (o DatasetGroupDomainPtrOutput) ToDatasetGroupDomainPtrOutput() DatasetGroupDomainPtrOutput {
	return o
}

func (o DatasetGroupDomainPtrOutput) ToDatasetGroupDomainPtrOutputWithContext(ctx context.Context) DatasetGroupDomainPtrOutput {
	return o
}

func (o DatasetGroupDomainPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*DatasetGroupDomain] {
	return pulumix.Output[*DatasetGroupDomain]{
		OutputState: o.OutputState,
	}
}

func (o DatasetGroupDomainPtrOutput) Elem() DatasetGroupDomainOutput {
	return o.ApplyT(func(v *DatasetGroupDomain) DatasetGroupDomain {
		if v != nil {
			return *v
		}
		var ret DatasetGroupDomain
		return ret
	}).(DatasetGroupDomainOutput)
}

func (o DatasetGroupDomainPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DatasetGroupDomainPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *DatasetGroupDomain) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// DatasetGroupDomainInput is an input type that accepts DatasetGroupDomainArgs and DatasetGroupDomainOutput values.
// You can construct a concrete instance of `DatasetGroupDomainInput` via:
//
//	DatasetGroupDomainArgs{...}
type DatasetGroupDomainInput interface {
	pulumi.Input

	ToDatasetGroupDomainOutput() DatasetGroupDomainOutput
	ToDatasetGroupDomainOutputWithContext(context.Context) DatasetGroupDomainOutput
}

var datasetGroupDomainPtrType = reflect.TypeOf((**DatasetGroupDomain)(nil)).Elem()

type DatasetGroupDomainPtrInput interface {
	pulumi.Input

	ToDatasetGroupDomainPtrOutput() DatasetGroupDomainPtrOutput
	ToDatasetGroupDomainPtrOutputWithContext(context.Context) DatasetGroupDomainPtrOutput
}

type datasetGroupDomainPtr string

func DatasetGroupDomainPtr(v string) DatasetGroupDomainPtrInput {
	return (*datasetGroupDomainPtr)(&v)
}

func (*datasetGroupDomainPtr) ElementType() reflect.Type {
	return datasetGroupDomainPtrType
}

func (in *datasetGroupDomainPtr) ToDatasetGroupDomainPtrOutput() DatasetGroupDomainPtrOutput {
	return pulumi.ToOutput(in).(DatasetGroupDomainPtrOutput)
}

func (in *datasetGroupDomainPtr) ToDatasetGroupDomainPtrOutputWithContext(ctx context.Context) DatasetGroupDomainPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(DatasetGroupDomainPtrOutput)
}

func (in *datasetGroupDomainPtr) ToOutput(ctx context.Context) pulumix.Output[*DatasetGroupDomain] {
	return pulumix.Output[*DatasetGroupDomain]{
		OutputState: in.ToDatasetGroupDomainPtrOutputWithContext(ctx).OutputState,
	}
}

// The dataset type
type DatasetType string

const (
	DatasetTypeTargetTimeSeries  = DatasetType("TARGET_TIME_SERIES")
	DatasetTypeRelatedTimeSeries = DatasetType("RELATED_TIME_SERIES")
	DatasetTypeItemMetadata      = DatasetType("ITEM_METADATA")
)

func (DatasetType) ElementType() reflect.Type {
	return reflect.TypeOf((*DatasetType)(nil)).Elem()
}

func (e DatasetType) ToDatasetTypeOutput() DatasetTypeOutput {
	return pulumi.ToOutput(e).(DatasetTypeOutput)
}

func (e DatasetType) ToDatasetTypeOutputWithContext(ctx context.Context) DatasetTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(DatasetTypeOutput)
}

func (e DatasetType) ToDatasetTypePtrOutput() DatasetTypePtrOutput {
	return e.ToDatasetTypePtrOutputWithContext(context.Background())
}

func (e DatasetType) ToDatasetTypePtrOutputWithContext(ctx context.Context) DatasetTypePtrOutput {
	return DatasetType(e).ToDatasetTypeOutputWithContext(ctx).ToDatasetTypePtrOutputWithContext(ctx)
}

func (e DatasetType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e DatasetType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e DatasetType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e DatasetType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type DatasetTypeOutput struct{ *pulumi.OutputState }

func (DatasetTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DatasetType)(nil)).Elem()
}

func (o DatasetTypeOutput) ToDatasetTypeOutput() DatasetTypeOutput {
	return o
}

func (o DatasetTypeOutput) ToDatasetTypeOutputWithContext(ctx context.Context) DatasetTypeOutput {
	return o
}

func (o DatasetTypeOutput) ToDatasetTypePtrOutput() DatasetTypePtrOutput {
	return o.ToDatasetTypePtrOutputWithContext(context.Background())
}

func (o DatasetTypeOutput) ToDatasetTypePtrOutputWithContext(ctx context.Context) DatasetTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DatasetType) *DatasetType {
		return &v
	}).(DatasetTypePtrOutput)
}

func (o DatasetTypeOutput) ToOutput(ctx context.Context) pulumix.Output[DatasetType] {
	return pulumix.Output[DatasetType]{
		OutputState: o.OutputState,
	}
}

func (o DatasetTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o DatasetTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DatasetType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o DatasetTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DatasetTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DatasetType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type DatasetTypePtrOutput struct{ *pulumi.OutputState }

func (DatasetTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DatasetType)(nil)).Elem()
}

func (o DatasetTypePtrOutput) ToDatasetTypePtrOutput() DatasetTypePtrOutput {
	return o
}

func (o DatasetTypePtrOutput) ToDatasetTypePtrOutputWithContext(ctx context.Context) DatasetTypePtrOutput {
	return o
}

func (o DatasetTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*DatasetType] {
	return pulumix.Output[*DatasetType]{
		OutputState: o.OutputState,
	}
}

func (o DatasetTypePtrOutput) Elem() DatasetTypeOutput {
	return o.ApplyT(func(v *DatasetType) DatasetType {
		if v != nil {
			return *v
		}
		var ret DatasetType
		return ret
	}).(DatasetTypeOutput)
}

func (o DatasetTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DatasetTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *DatasetType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// DatasetTypeInput is an input type that accepts DatasetTypeArgs and DatasetTypeOutput values.
// You can construct a concrete instance of `DatasetTypeInput` via:
//
//	DatasetTypeArgs{...}
type DatasetTypeInput interface {
	pulumi.Input

	ToDatasetTypeOutput() DatasetTypeOutput
	ToDatasetTypeOutputWithContext(context.Context) DatasetTypeOutput
}

var datasetTypePtrType = reflect.TypeOf((**DatasetType)(nil)).Elem()

type DatasetTypePtrInput interface {
	pulumi.Input

	ToDatasetTypePtrOutput() DatasetTypePtrOutput
	ToDatasetTypePtrOutputWithContext(context.Context) DatasetTypePtrOutput
}

type datasetTypePtr string

func DatasetTypePtr(v string) DatasetTypePtrInput {
	return (*datasetTypePtr)(&v)
}

func (*datasetTypePtr) ElementType() reflect.Type {
	return datasetTypePtrType
}

func (in *datasetTypePtr) ToDatasetTypePtrOutput() DatasetTypePtrOutput {
	return pulumi.ToOutput(in).(DatasetTypePtrOutput)
}

func (in *datasetTypePtr) ToDatasetTypePtrOutputWithContext(ctx context.Context) DatasetTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(DatasetTypePtrOutput)
}

func (in *datasetTypePtr) ToOutput(ctx context.Context) pulumix.Output[*DatasetType] {
	return pulumix.Output[*DatasetType]{
		OutputState: in.ToDatasetTypePtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DatasetAttributesItemPropertiesAttributeTypeInput)(nil)).Elem(), DatasetAttributesItemPropertiesAttributeType("string"))
	pulumi.RegisterInputType(reflect.TypeOf((*DatasetAttributesItemPropertiesAttributeTypePtrInput)(nil)).Elem(), DatasetAttributesItemPropertiesAttributeType("string"))
	pulumi.RegisterInputType(reflect.TypeOf((*DatasetDomainInput)(nil)).Elem(), DatasetDomain("RETAIL"))
	pulumi.RegisterInputType(reflect.TypeOf((*DatasetDomainPtrInput)(nil)).Elem(), DatasetDomain("RETAIL"))
	pulumi.RegisterInputType(reflect.TypeOf((*DatasetGroupDomainInput)(nil)).Elem(), DatasetGroupDomain("RETAIL"))
	pulumi.RegisterInputType(reflect.TypeOf((*DatasetGroupDomainPtrInput)(nil)).Elem(), DatasetGroupDomain("RETAIL"))
	pulumi.RegisterInputType(reflect.TypeOf((*DatasetTypeInput)(nil)).Elem(), DatasetType("TARGET_TIME_SERIES"))
	pulumi.RegisterInputType(reflect.TypeOf((*DatasetTypePtrInput)(nil)).Elem(), DatasetType("TARGET_TIME_SERIES"))
	pulumi.RegisterOutputType(DatasetAttributesItemPropertiesAttributeTypeOutput{})
	pulumi.RegisterOutputType(DatasetAttributesItemPropertiesAttributeTypePtrOutput{})
	pulumi.RegisterOutputType(DatasetDomainOutput{})
	pulumi.RegisterOutputType(DatasetDomainPtrOutput{})
	pulumi.RegisterOutputType(DatasetGroupDomainOutput{})
	pulumi.RegisterOutputType(DatasetGroupDomainPtrOutput{})
	pulumi.RegisterOutputType(DatasetTypeOutput{})
	pulumi.RegisterOutputType(DatasetTypePtrOutput{})
}
