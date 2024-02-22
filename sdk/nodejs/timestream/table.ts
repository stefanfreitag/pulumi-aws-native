// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::Timestream::Table resource creates a Timestream Table.
 */
export class Table extends pulumi.CustomResource {
    /**
     * Get an existing Table resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Table {
        return new Table(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:timestream:Table';

    /**
     * Returns true if the given object is an instance of Table.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Table {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Table.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The name for the database which the table to be created belongs to.
     */
    public readonly databaseName!: pulumi.Output<string>;
    /**
     * The properties that determine whether magnetic store writes are enabled.
     */
    public readonly magneticStoreWriteProperties!: pulumi.Output<outputs.timestream.MagneticStoreWritePropertiesProperties | undefined>;
    /**
     * The table name exposed as a read-only attribute.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The retention duration of the memory store and the magnetic store.
     */
    public readonly retentionProperties!: pulumi.Output<outputs.timestream.RetentionPropertiesProperties | undefined>;
    /**
     * A Schema specifies the expected data model of the table.
     */
    public readonly schema!: pulumi.Output<outputs.timestream.SchemaProperties | undefined>;
    /**
     * The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.
     */
    public readonly tableName!: pulumi.Output<string | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a Table resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TableArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.databaseName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'databaseName'");
            }
            resourceInputs["databaseName"] = args ? args.databaseName : undefined;
            resourceInputs["magneticStoreWriteProperties"] = args ? args.magneticStoreWriteProperties : undefined;
            resourceInputs["retentionProperties"] = args ? args.retentionProperties : undefined;
            resourceInputs["schema"] = args ? args.schema : undefined;
            resourceInputs["tableName"] = args ? args.tableName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["databaseName"] = undefined /*out*/;
            resourceInputs["magneticStoreWriteProperties"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["retentionProperties"] = undefined /*out*/;
            resourceInputs["schema"] = undefined /*out*/;
            resourceInputs["tableName"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["databaseName", "tableName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Table.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Table resource.
 */
export interface TableArgs {
    /**
     * The name for the database which the table to be created belongs to.
     */
    databaseName: pulumi.Input<string>;
    /**
     * The properties that determine whether magnetic store writes are enabled.
     */
    magneticStoreWriteProperties?: pulumi.Input<inputs.timestream.MagneticStoreWritePropertiesPropertiesArgs>;
    /**
     * The retention duration of the memory store and the magnetic store.
     */
    retentionProperties?: pulumi.Input<inputs.timestream.RetentionPropertiesPropertiesArgs>;
    /**
     * A Schema specifies the expected data model of the table.
     */
    schema?: pulumi.Input<inputs.timestream.SchemaPropertiesArgs>;
    /**
     * The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.
     */
    tableName?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
