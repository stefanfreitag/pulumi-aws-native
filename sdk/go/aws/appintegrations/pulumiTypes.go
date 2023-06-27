// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appintegrations

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The configuration for what files should be pulled from the source.
type DataIntegrationFileConfiguration struct {
	// Restrictions for what files should be pulled from the source.
	Filters interface{} `pulumi:"filters"`
	// Identifiers for the source folders to pull all files from recursively.
	Folders []string `pulumi:"folders"`
}

// DataIntegrationFileConfigurationInput is an input type that accepts DataIntegrationFileConfigurationArgs and DataIntegrationFileConfigurationOutput values.
// You can construct a concrete instance of `DataIntegrationFileConfigurationInput` via:
//
//	DataIntegrationFileConfigurationArgs{...}
type DataIntegrationFileConfigurationInput interface {
	pulumi.Input

	ToDataIntegrationFileConfigurationOutput() DataIntegrationFileConfigurationOutput
	ToDataIntegrationFileConfigurationOutputWithContext(context.Context) DataIntegrationFileConfigurationOutput
}

// The configuration for what files should be pulled from the source.
type DataIntegrationFileConfigurationArgs struct {
	// Restrictions for what files should be pulled from the source.
	Filters pulumi.Input `pulumi:"filters"`
	// Identifiers for the source folders to pull all files from recursively.
	Folders pulumi.StringArrayInput `pulumi:"folders"`
}

func (DataIntegrationFileConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DataIntegrationFileConfiguration)(nil)).Elem()
}

func (i DataIntegrationFileConfigurationArgs) ToDataIntegrationFileConfigurationOutput() DataIntegrationFileConfigurationOutput {
	return i.ToDataIntegrationFileConfigurationOutputWithContext(context.Background())
}

func (i DataIntegrationFileConfigurationArgs) ToDataIntegrationFileConfigurationOutputWithContext(ctx context.Context) DataIntegrationFileConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataIntegrationFileConfigurationOutput)
}

func (i DataIntegrationFileConfigurationArgs) ToDataIntegrationFileConfigurationPtrOutput() DataIntegrationFileConfigurationPtrOutput {
	return i.ToDataIntegrationFileConfigurationPtrOutputWithContext(context.Background())
}

func (i DataIntegrationFileConfigurationArgs) ToDataIntegrationFileConfigurationPtrOutputWithContext(ctx context.Context) DataIntegrationFileConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataIntegrationFileConfigurationOutput).ToDataIntegrationFileConfigurationPtrOutputWithContext(ctx)
}

// DataIntegrationFileConfigurationPtrInput is an input type that accepts DataIntegrationFileConfigurationArgs, DataIntegrationFileConfigurationPtr and DataIntegrationFileConfigurationPtrOutput values.
// You can construct a concrete instance of `DataIntegrationFileConfigurationPtrInput` via:
//
//	        DataIntegrationFileConfigurationArgs{...}
//
//	or:
//
//	        nil
type DataIntegrationFileConfigurationPtrInput interface {
	pulumi.Input

	ToDataIntegrationFileConfigurationPtrOutput() DataIntegrationFileConfigurationPtrOutput
	ToDataIntegrationFileConfigurationPtrOutputWithContext(context.Context) DataIntegrationFileConfigurationPtrOutput
}

type dataIntegrationFileConfigurationPtrType DataIntegrationFileConfigurationArgs

func DataIntegrationFileConfigurationPtr(v *DataIntegrationFileConfigurationArgs) DataIntegrationFileConfigurationPtrInput {
	return (*dataIntegrationFileConfigurationPtrType)(v)
}

func (*dataIntegrationFileConfigurationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**DataIntegrationFileConfiguration)(nil)).Elem()
}

func (i *dataIntegrationFileConfigurationPtrType) ToDataIntegrationFileConfigurationPtrOutput() DataIntegrationFileConfigurationPtrOutput {
	return i.ToDataIntegrationFileConfigurationPtrOutputWithContext(context.Background())
}

func (i *dataIntegrationFileConfigurationPtrType) ToDataIntegrationFileConfigurationPtrOutputWithContext(ctx context.Context) DataIntegrationFileConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataIntegrationFileConfigurationPtrOutput)
}

// The configuration for what files should be pulled from the source.
type DataIntegrationFileConfigurationOutput struct{ *pulumi.OutputState }

func (DataIntegrationFileConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DataIntegrationFileConfiguration)(nil)).Elem()
}

func (o DataIntegrationFileConfigurationOutput) ToDataIntegrationFileConfigurationOutput() DataIntegrationFileConfigurationOutput {
	return o
}

func (o DataIntegrationFileConfigurationOutput) ToDataIntegrationFileConfigurationOutputWithContext(ctx context.Context) DataIntegrationFileConfigurationOutput {
	return o
}

func (o DataIntegrationFileConfigurationOutput) ToDataIntegrationFileConfigurationPtrOutput() DataIntegrationFileConfigurationPtrOutput {
	return o.ToDataIntegrationFileConfigurationPtrOutputWithContext(context.Background())
}

func (o DataIntegrationFileConfigurationOutput) ToDataIntegrationFileConfigurationPtrOutputWithContext(ctx context.Context) DataIntegrationFileConfigurationPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DataIntegrationFileConfiguration) *DataIntegrationFileConfiguration {
		return &v
	}).(DataIntegrationFileConfigurationPtrOutput)
}

// Restrictions for what files should be pulled from the source.
func (o DataIntegrationFileConfigurationOutput) Filters() pulumi.AnyOutput {
	return o.ApplyT(func(v DataIntegrationFileConfiguration) interface{} { return v.Filters }).(pulumi.AnyOutput)
}

// Identifiers for the source folders to pull all files from recursively.
func (o DataIntegrationFileConfigurationOutput) Folders() pulumi.StringArrayOutput {
	return o.ApplyT(func(v DataIntegrationFileConfiguration) []string { return v.Folders }).(pulumi.StringArrayOutput)
}

type DataIntegrationFileConfigurationPtrOutput struct{ *pulumi.OutputState }

func (DataIntegrationFileConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DataIntegrationFileConfiguration)(nil)).Elem()
}

func (o DataIntegrationFileConfigurationPtrOutput) ToDataIntegrationFileConfigurationPtrOutput() DataIntegrationFileConfigurationPtrOutput {
	return o
}

func (o DataIntegrationFileConfigurationPtrOutput) ToDataIntegrationFileConfigurationPtrOutputWithContext(ctx context.Context) DataIntegrationFileConfigurationPtrOutput {
	return o
}

func (o DataIntegrationFileConfigurationPtrOutput) Elem() DataIntegrationFileConfigurationOutput {
	return o.ApplyT(func(v *DataIntegrationFileConfiguration) DataIntegrationFileConfiguration {
		if v != nil {
			return *v
		}
		var ret DataIntegrationFileConfiguration
		return ret
	}).(DataIntegrationFileConfigurationOutput)
}

// Restrictions for what files should be pulled from the source.
func (o DataIntegrationFileConfigurationPtrOutput) Filters() pulumi.AnyOutput {
	return o.ApplyT(func(v *DataIntegrationFileConfiguration) interface{} {
		if v == nil {
			return nil
		}
		return v.Filters
	}).(pulumi.AnyOutput)
}

// Identifiers for the source folders to pull all files from recursively.
func (o DataIntegrationFileConfigurationPtrOutput) Folders() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *DataIntegrationFileConfiguration) []string {
		if v == nil {
			return nil
		}
		return v.Folders
	}).(pulumi.StringArrayOutput)
}

// The configuration for what data should be pulled from the source.
type DataIntegrationObjectConfiguration struct {
}

// DataIntegrationObjectConfigurationInput is an input type that accepts DataIntegrationObjectConfigurationArgs and DataIntegrationObjectConfigurationOutput values.
// You can construct a concrete instance of `DataIntegrationObjectConfigurationInput` via:
//
//	DataIntegrationObjectConfigurationArgs{...}
type DataIntegrationObjectConfigurationInput interface {
	pulumi.Input

	ToDataIntegrationObjectConfigurationOutput() DataIntegrationObjectConfigurationOutput
	ToDataIntegrationObjectConfigurationOutputWithContext(context.Context) DataIntegrationObjectConfigurationOutput
}

// The configuration for what data should be pulled from the source.
type DataIntegrationObjectConfigurationArgs struct {
}

func (DataIntegrationObjectConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DataIntegrationObjectConfiguration)(nil)).Elem()
}

func (i DataIntegrationObjectConfigurationArgs) ToDataIntegrationObjectConfigurationOutput() DataIntegrationObjectConfigurationOutput {
	return i.ToDataIntegrationObjectConfigurationOutputWithContext(context.Background())
}

func (i DataIntegrationObjectConfigurationArgs) ToDataIntegrationObjectConfigurationOutputWithContext(ctx context.Context) DataIntegrationObjectConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataIntegrationObjectConfigurationOutput)
}

func (i DataIntegrationObjectConfigurationArgs) ToDataIntegrationObjectConfigurationPtrOutput() DataIntegrationObjectConfigurationPtrOutput {
	return i.ToDataIntegrationObjectConfigurationPtrOutputWithContext(context.Background())
}

func (i DataIntegrationObjectConfigurationArgs) ToDataIntegrationObjectConfigurationPtrOutputWithContext(ctx context.Context) DataIntegrationObjectConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataIntegrationObjectConfigurationOutput).ToDataIntegrationObjectConfigurationPtrOutputWithContext(ctx)
}

// DataIntegrationObjectConfigurationPtrInput is an input type that accepts DataIntegrationObjectConfigurationArgs, DataIntegrationObjectConfigurationPtr and DataIntegrationObjectConfigurationPtrOutput values.
// You can construct a concrete instance of `DataIntegrationObjectConfigurationPtrInput` via:
//
//	        DataIntegrationObjectConfigurationArgs{...}
//
//	or:
//
//	        nil
type DataIntegrationObjectConfigurationPtrInput interface {
	pulumi.Input

	ToDataIntegrationObjectConfigurationPtrOutput() DataIntegrationObjectConfigurationPtrOutput
	ToDataIntegrationObjectConfigurationPtrOutputWithContext(context.Context) DataIntegrationObjectConfigurationPtrOutput
}

type dataIntegrationObjectConfigurationPtrType DataIntegrationObjectConfigurationArgs

func DataIntegrationObjectConfigurationPtr(v *DataIntegrationObjectConfigurationArgs) DataIntegrationObjectConfigurationPtrInput {
	return (*dataIntegrationObjectConfigurationPtrType)(v)
}

func (*dataIntegrationObjectConfigurationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**DataIntegrationObjectConfiguration)(nil)).Elem()
}

func (i *dataIntegrationObjectConfigurationPtrType) ToDataIntegrationObjectConfigurationPtrOutput() DataIntegrationObjectConfigurationPtrOutput {
	return i.ToDataIntegrationObjectConfigurationPtrOutputWithContext(context.Background())
}

func (i *dataIntegrationObjectConfigurationPtrType) ToDataIntegrationObjectConfigurationPtrOutputWithContext(ctx context.Context) DataIntegrationObjectConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataIntegrationObjectConfigurationPtrOutput)
}

// The configuration for what data should be pulled from the source.
type DataIntegrationObjectConfigurationOutput struct{ *pulumi.OutputState }

func (DataIntegrationObjectConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DataIntegrationObjectConfiguration)(nil)).Elem()
}

func (o DataIntegrationObjectConfigurationOutput) ToDataIntegrationObjectConfigurationOutput() DataIntegrationObjectConfigurationOutput {
	return o
}

func (o DataIntegrationObjectConfigurationOutput) ToDataIntegrationObjectConfigurationOutputWithContext(ctx context.Context) DataIntegrationObjectConfigurationOutput {
	return o
}

func (o DataIntegrationObjectConfigurationOutput) ToDataIntegrationObjectConfigurationPtrOutput() DataIntegrationObjectConfigurationPtrOutput {
	return o.ToDataIntegrationObjectConfigurationPtrOutputWithContext(context.Background())
}

func (o DataIntegrationObjectConfigurationOutput) ToDataIntegrationObjectConfigurationPtrOutputWithContext(ctx context.Context) DataIntegrationObjectConfigurationPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DataIntegrationObjectConfiguration) *DataIntegrationObjectConfiguration {
		return &v
	}).(DataIntegrationObjectConfigurationPtrOutput)
}

type DataIntegrationObjectConfigurationPtrOutput struct{ *pulumi.OutputState }

func (DataIntegrationObjectConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DataIntegrationObjectConfiguration)(nil)).Elem()
}

func (o DataIntegrationObjectConfigurationPtrOutput) ToDataIntegrationObjectConfigurationPtrOutput() DataIntegrationObjectConfigurationPtrOutput {
	return o
}

func (o DataIntegrationObjectConfigurationPtrOutput) ToDataIntegrationObjectConfigurationPtrOutputWithContext(ctx context.Context) DataIntegrationObjectConfigurationPtrOutput {
	return o
}

func (o DataIntegrationObjectConfigurationPtrOutput) Elem() DataIntegrationObjectConfigurationOutput {
	return o.ApplyT(func(v *DataIntegrationObjectConfiguration) DataIntegrationObjectConfiguration {
		if v != nil {
			return *v
		}
		var ret DataIntegrationObjectConfiguration
		return ret
	}).(DataIntegrationObjectConfigurationOutput)
}

type DataIntegrationScheduleConfig struct {
	// The start date for objects to import in the first flow run. Epoch or ISO timestamp format is supported.
	FirstExecutionFrom *string `pulumi:"firstExecutionFrom"`
	// The name of the object to pull from the data source.
	Object *string `pulumi:"object"`
	// How often the data should be pulled from data source.
	ScheduleExpression string `pulumi:"scheduleExpression"`
}

// DataIntegrationScheduleConfigInput is an input type that accepts DataIntegrationScheduleConfigArgs and DataIntegrationScheduleConfigOutput values.
// You can construct a concrete instance of `DataIntegrationScheduleConfigInput` via:
//
//	DataIntegrationScheduleConfigArgs{...}
type DataIntegrationScheduleConfigInput interface {
	pulumi.Input

	ToDataIntegrationScheduleConfigOutput() DataIntegrationScheduleConfigOutput
	ToDataIntegrationScheduleConfigOutputWithContext(context.Context) DataIntegrationScheduleConfigOutput
}

type DataIntegrationScheduleConfigArgs struct {
	// The start date for objects to import in the first flow run. Epoch or ISO timestamp format is supported.
	FirstExecutionFrom pulumi.StringPtrInput `pulumi:"firstExecutionFrom"`
	// The name of the object to pull from the data source.
	Object pulumi.StringPtrInput `pulumi:"object"`
	// How often the data should be pulled from data source.
	ScheduleExpression pulumi.StringInput `pulumi:"scheduleExpression"`
}

func (DataIntegrationScheduleConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DataIntegrationScheduleConfig)(nil)).Elem()
}

func (i DataIntegrationScheduleConfigArgs) ToDataIntegrationScheduleConfigOutput() DataIntegrationScheduleConfigOutput {
	return i.ToDataIntegrationScheduleConfigOutputWithContext(context.Background())
}

func (i DataIntegrationScheduleConfigArgs) ToDataIntegrationScheduleConfigOutputWithContext(ctx context.Context) DataIntegrationScheduleConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataIntegrationScheduleConfigOutput)
}

type DataIntegrationScheduleConfigOutput struct{ *pulumi.OutputState }

func (DataIntegrationScheduleConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DataIntegrationScheduleConfig)(nil)).Elem()
}

func (o DataIntegrationScheduleConfigOutput) ToDataIntegrationScheduleConfigOutput() DataIntegrationScheduleConfigOutput {
	return o
}

func (o DataIntegrationScheduleConfigOutput) ToDataIntegrationScheduleConfigOutputWithContext(ctx context.Context) DataIntegrationScheduleConfigOutput {
	return o
}

// The start date for objects to import in the first flow run. Epoch or ISO timestamp format is supported.
func (o DataIntegrationScheduleConfigOutput) FirstExecutionFrom() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataIntegrationScheduleConfig) *string { return v.FirstExecutionFrom }).(pulumi.StringPtrOutput)
}

// The name of the object to pull from the data source.
func (o DataIntegrationScheduleConfigOutput) Object() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataIntegrationScheduleConfig) *string { return v.Object }).(pulumi.StringPtrOutput)
}

// How often the data should be pulled from data source.
func (o DataIntegrationScheduleConfigOutput) ScheduleExpression() pulumi.StringOutput {
	return o.ApplyT(func(v DataIntegrationScheduleConfig) string { return v.ScheduleExpression }).(pulumi.StringOutput)
}

// A label for tagging DataIntegration resources
type DataIntegrationTag struct {
	// A key to identify the tag.
	Key string `pulumi:"key"`
	// Corresponding tag value for the key.
	Value string `pulumi:"value"`
}

// DataIntegrationTagInput is an input type that accepts DataIntegrationTagArgs and DataIntegrationTagOutput values.
// You can construct a concrete instance of `DataIntegrationTagInput` via:
//
//	DataIntegrationTagArgs{...}
type DataIntegrationTagInput interface {
	pulumi.Input

	ToDataIntegrationTagOutput() DataIntegrationTagOutput
	ToDataIntegrationTagOutputWithContext(context.Context) DataIntegrationTagOutput
}

// A label for tagging DataIntegration resources
type DataIntegrationTagArgs struct {
	// A key to identify the tag.
	Key pulumi.StringInput `pulumi:"key"`
	// Corresponding tag value for the key.
	Value pulumi.StringInput `pulumi:"value"`
}

func (DataIntegrationTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DataIntegrationTag)(nil)).Elem()
}

func (i DataIntegrationTagArgs) ToDataIntegrationTagOutput() DataIntegrationTagOutput {
	return i.ToDataIntegrationTagOutputWithContext(context.Background())
}

func (i DataIntegrationTagArgs) ToDataIntegrationTagOutputWithContext(ctx context.Context) DataIntegrationTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataIntegrationTagOutput)
}

// DataIntegrationTagArrayInput is an input type that accepts DataIntegrationTagArray and DataIntegrationTagArrayOutput values.
// You can construct a concrete instance of `DataIntegrationTagArrayInput` via:
//
//	DataIntegrationTagArray{ DataIntegrationTagArgs{...} }
type DataIntegrationTagArrayInput interface {
	pulumi.Input

	ToDataIntegrationTagArrayOutput() DataIntegrationTagArrayOutput
	ToDataIntegrationTagArrayOutputWithContext(context.Context) DataIntegrationTagArrayOutput
}

type DataIntegrationTagArray []DataIntegrationTagInput

func (DataIntegrationTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]DataIntegrationTag)(nil)).Elem()
}

func (i DataIntegrationTagArray) ToDataIntegrationTagArrayOutput() DataIntegrationTagArrayOutput {
	return i.ToDataIntegrationTagArrayOutputWithContext(context.Background())
}

func (i DataIntegrationTagArray) ToDataIntegrationTagArrayOutputWithContext(ctx context.Context) DataIntegrationTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataIntegrationTagArrayOutput)
}

// A label for tagging DataIntegration resources
type DataIntegrationTagOutput struct{ *pulumi.OutputState }

func (DataIntegrationTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DataIntegrationTag)(nil)).Elem()
}

func (o DataIntegrationTagOutput) ToDataIntegrationTagOutput() DataIntegrationTagOutput {
	return o
}

func (o DataIntegrationTagOutput) ToDataIntegrationTagOutputWithContext(ctx context.Context) DataIntegrationTagOutput {
	return o
}

// A key to identify the tag.
func (o DataIntegrationTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v DataIntegrationTag) string { return v.Key }).(pulumi.StringOutput)
}

// Corresponding tag value for the key.
func (o DataIntegrationTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v DataIntegrationTag) string { return v.Value }).(pulumi.StringOutput)
}

type DataIntegrationTagArrayOutput struct{ *pulumi.OutputState }

func (DataIntegrationTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]DataIntegrationTag)(nil)).Elem()
}

func (o DataIntegrationTagArrayOutput) ToDataIntegrationTagArrayOutput() DataIntegrationTagArrayOutput {
	return o
}

func (o DataIntegrationTagArrayOutput) ToDataIntegrationTagArrayOutputWithContext(ctx context.Context) DataIntegrationTagArrayOutput {
	return o
}

func (o DataIntegrationTagArrayOutput) Index(i pulumi.IntInput) DataIntegrationTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) DataIntegrationTag {
		return vs[0].([]DataIntegrationTag)[vs[1].(int)]
	}).(DataIntegrationTagOutput)
}

type EventIntegrationEventFilter struct {
	// The source of the events.
	Source string `pulumi:"source"`
}

// EventIntegrationEventFilterInput is an input type that accepts EventIntegrationEventFilterArgs and EventIntegrationEventFilterOutput values.
// You can construct a concrete instance of `EventIntegrationEventFilterInput` via:
//
//	EventIntegrationEventFilterArgs{...}
type EventIntegrationEventFilterInput interface {
	pulumi.Input

	ToEventIntegrationEventFilterOutput() EventIntegrationEventFilterOutput
	ToEventIntegrationEventFilterOutputWithContext(context.Context) EventIntegrationEventFilterOutput
}

type EventIntegrationEventFilterArgs struct {
	// The source of the events.
	Source pulumi.StringInput `pulumi:"source"`
}

func (EventIntegrationEventFilterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*EventIntegrationEventFilter)(nil)).Elem()
}

func (i EventIntegrationEventFilterArgs) ToEventIntegrationEventFilterOutput() EventIntegrationEventFilterOutput {
	return i.ToEventIntegrationEventFilterOutputWithContext(context.Background())
}

func (i EventIntegrationEventFilterArgs) ToEventIntegrationEventFilterOutputWithContext(ctx context.Context) EventIntegrationEventFilterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EventIntegrationEventFilterOutput)
}

type EventIntegrationEventFilterOutput struct{ *pulumi.OutputState }

func (EventIntegrationEventFilterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EventIntegrationEventFilter)(nil)).Elem()
}

func (o EventIntegrationEventFilterOutput) ToEventIntegrationEventFilterOutput() EventIntegrationEventFilterOutput {
	return o
}

func (o EventIntegrationEventFilterOutput) ToEventIntegrationEventFilterOutputWithContext(ctx context.Context) EventIntegrationEventFilterOutput {
	return o
}

// The source of the events.
func (o EventIntegrationEventFilterOutput) Source() pulumi.StringOutput {
	return o.ApplyT(func(v EventIntegrationEventFilter) string { return v.Source }).(pulumi.StringOutput)
}

type EventIntegrationTag struct {
	// A key to identify the tag.
	Key string `pulumi:"key"`
	// Corresponding tag value for the key.
	Value string `pulumi:"value"`
}

// EventIntegrationTagInput is an input type that accepts EventIntegrationTagArgs and EventIntegrationTagOutput values.
// You can construct a concrete instance of `EventIntegrationTagInput` via:
//
//	EventIntegrationTagArgs{...}
type EventIntegrationTagInput interface {
	pulumi.Input

	ToEventIntegrationTagOutput() EventIntegrationTagOutput
	ToEventIntegrationTagOutputWithContext(context.Context) EventIntegrationTagOutput
}

type EventIntegrationTagArgs struct {
	// A key to identify the tag.
	Key pulumi.StringInput `pulumi:"key"`
	// Corresponding tag value for the key.
	Value pulumi.StringInput `pulumi:"value"`
}

func (EventIntegrationTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*EventIntegrationTag)(nil)).Elem()
}

func (i EventIntegrationTagArgs) ToEventIntegrationTagOutput() EventIntegrationTagOutput {
	return i.ToEventIntegrationTagOutputWithContext(context.Background())
}

func (i EventIntegrationTagArgs) ToEventIntegrationTagOutputWithContext(ctx context.Context) EventIntegrationTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EventIntegrationTagOutput)
}

// EventIntegrationTagArrayInput is an input type that accepts EventIntegrationTagArray and EventIntegrationTagArrayOutput values.
// You can construct a concrete instance of `EventIntegrationTagArrayInput` via:
//
//	EventIntegrationTagArray{ EventIntegrationTagArgs{...} }
type EventIntegrationTagArrayInput interface {
	pulumi.Input

	ToEventIntegrationTagArrayOutput() EventIntegrationTagArrayOutput
	ToEventIntegrationTagArrayOutputWithContext(context.Context) EventIntegrationTagArrayOutput
}

type EventIntegrationTagArray []EventIntegrationTagInput

func (EventIntegrationTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EventIntegrationTag)(nil)).Elem()
}

func (i EventIntegrationTagArray) ToEventIntegrationTagArrayOutput() EventIntegrationTagArrayOutput {
	return i.ToEventIntegrationTagArrayOutputWithContext(context.Background())
}

func (i EventIntegrationTagArray) ToEventIntegrationTagArrayOutputWithContext(ctx context.Context) EventIntegrationTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EventIntegrationTagArrayOutput)
}

type EventIntegrationTagOutput struct{ *pulumi.OutputState }

func (EventIntegrationTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EventIntegrationTag)(nil)).Elem()
}

func (o EventIntegrationTagOutput) ToEventIntegrationTagOutput() EventIntegrationTagOutput {
	return o
}

func (o EventIntegrationTagOutput) ToEventIntegrationTagOutputWithContext(ctx context.Context) EventIntegrationTagOutput {
	return o
}

// A key to identify the tag.
func (o EventIntegrationTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v EventIntegrationTag) string { return v.Key }).(pulumi.StringOutput)
}

// Corresponding tag value for the key.
func (o EventIntegrationTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v EventIntegrationTag) string { return v.Value }).(pulumi.StringOutput)
}

type EventIntegrationTagArrayOutput struct{ *pulumi.OutputState }

func (EventIntegrationTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EventIntegrationTag)(nil)).Elem()
}

func (o EventIntegrationTagArrayOutput) ToEventIntegrationTagArrayOutput() EventIntegrationTagArrayOutput {
	return o
}

func (o EventIntegrationTagArrayOutput) ToEventIntegrationTagArrayOutputWithContext(ctx context.Context) EventIntegrationTagArrayOutput {
	return o
}

func (o EventIntegrationTagArrayOutput) Index(i pulumi.IntInput) EventIntegrationTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) EventIntegrationTag {
		return vs[0].([]EventIntegrationTag)[vs[1].(int)]
	}).(EventIntegrationTagOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DataIntegrationFileConfigurationInput)(nil)).Elem(), DataIntegrationFileConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataIntegrationFileConfigurationPtrInput)(nil)).Elem(), DataIntegrationFileConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataIntegrationObjectConfigurationInput)(nil)).Elem(), DataIntegrationObjectConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataIntegrationObjectConfigurationPtrInput)(nil)).Elem(), DataIntegrationObjectConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataIntegrationScheduleConfigInput)(nil)).Elem(), DataIntegrationScheduleConfigArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataIntegrationTagInput)(nil)).Elem(), DataIntegrationTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataIntegrationTagArrayInput)(nil)).Elem(), DataIntegrationTagArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*EventIntegrationEventFilterInput)(nil)).Elem(), EventIntegrationEventFilterArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*EventIntegrationTagInput)(nil)).Elem(), EventIntegrationTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*EventIntegrationTagArrayInput)(nil)).Elem(), EventIntegrationTagArray{})
	pulumi.RegisterOutputType(DataIntegrationFileConfigurationOutput{})
	pulumi.RegisterOutputType(DataIntegrationFileConfigurationPtrOutput{})
	pulumi.RegisterOutputType(DataIntegrationObjectConfigurationOutput{})
	pulumi.RegisterOutputType(DataIntegrationObjectConfigurationPtrOutput{})
	pulumi.RegisterOutputType(DataIntegrationScheduleConfigOutput{})
	pulumi.RegisterOutputType(DataIntegrationTagOutput{})
	pulumi.RegisterOutputType(DataIntegrationTagArrayOutput{})
	pulumi.RegisterOutputType(EventIntegrationEventFilterOutput{})
	pulumi.RegisterOutputType(EventIntegrationTagOutput{})
	pulumi.RegisterOutputType(EventIntegrationTagArrayOutput{})
}
