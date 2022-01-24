// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::DMS::Endpoint
 *
 * @deprecated Endpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Endpoint extends pulumi.CustomResource {
    /**
     * Get an existing Endpoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Endpoint {
        pulumi.log.warn("Endpoint is deprecated: Endpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Endpoint(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:dms:Endpoint';

    /**
     * Returns true if the given object is an instance of Endpoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Endpoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Endpoint.__pulumiType;
    }

    public readonly certificateArn!: pulumi.Output<string | undefined>;
    public readonly databaseName!: pulumi.Output<string | undefined>;
    public readonly docDbSettings!: pulumi.Output<outputs.dms.EndpointDocDbSettings | undefined>;
    public readonly dynamoDbSettings!: pulumi.Output<outputs.dms.EndpointDynamoDbSettings | undefined>;
    public readonly elasticsearchSettings!: pulumi.Output<outputs.dms.EndpointElasticsearchSettings | undefined>;
    public readonly endpointIdentifier!: pulumi.Output<string | undefined>;
    public readonly endpointType!: pulumi.Output<string>;
    public readonly engineName!: pulumi.Output<string>;
    public /*out*/ readonly externalId!: pulumi.Output<string>;
    public readonly extraConnectionAttributes!: pulumi.Output<string | undefined>;
    public readonly gcpMySQLSettings!: pulumi.Output<outputs.dms.EndpointGcpMySQLSettings | undefined>;
    public readonly ibmDb2Settings!: pulumi.Output<outputs.dms.EndpointIbmDb2Settings | undefined>;
    public readonly kafkaSettings!: pulumi.Output<outputs.dms.EndpointKafkaSettings | undefined>;
    public readonly kinesisSettings!: pulumi.Output<outputs.dms.EndpointKinesisSettings | undefined>;
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    public readonly microsoftSqlServerSettings!: pulumi.Output<outputs.dms.EndpointMicrosoftSqlServerSettings | undefined>;
    public readonly mongoDbSettings!: pulumi.Output<outputs.dms.EndpointMongoDbSettings | undefined>;
    public readonly mySqlSettings!: pulumi.Output<outputs.dms.EndpointMySqlSettings | undefined>;
    public readonly neptuneSettings!: pulumi.Output<outputs.dms.EndpointNeptuneSettings | undefined>;
    public readonly oracleSettings!: pulumi.Output<outputs.dms.EndpointOracleSettings | undefined>;
    public readonly password!: pulumi.Output<string | undefined>;
    public readonly port!: pulumi.Output<number | undefined>;
    public readonly postgreSqlSettings!: pulumi.Output<outputs.dms.EndpointPostgreSqlSettings | undefined>;
    public readonly redisSettings!: pulumi.Output<outputs.dms.EndpointRedisSettings | undefined>;
    public readonly redshiftSettings!: pulumi.Output<outputs.dms.EndpointRedshiftSettings | undefined>;
    public readonly resourceIdentifier!: pulumi.Output<string | undefined>;
    public readonly s3Settings!: pulumi.Output<outputs.dms.EndpointS3Settings | undefined>;
    public readonly serverName!: pulumi.Output<string | undefined>;
    public readonly sslMode!: pulumi.Output<string | undefined>;
    public readonly sybaseSettings!: pulumi.Output<outputs.dms.EndpointSybaseSettings | undefined>;
    public readonly tags!: pulumi.Output<outputs.dms.EndpointTag[] | undefined>;
    public readonly username!: pulumi.Output<string | undefined>;

    /**
     * Create a Endpoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Endpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: EndpointArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Endpoint is deprecated: Endpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.endpointType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'endpointType'");
            }
            if ((!args || args.engineName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'engineName'");
            }
            inputs["certificateArn"] = args ? args.certificateArn : undefined;
            inputs["databaseName"] = args ? args.databaseName : undefined;
            inputs["docDbSettings"] = args ? args.docDbSettings : undefined;
            inputs["dynamoDbSettings"] = args ? args.dynamoDbSettings : undefined;
            inputs["elasticsearchSettings"] = args ? args.elasticsearchSettings : undefined;
            inputs["endpointIdentifier"] = args ? args.endpointIdentifier : undefined;
            inputs["endpointType"] = args ? args.endpointType : undefined;
            inputs["engineName"] = args ? args.engineName : undefined;
            inputs["extraConnectionAttributes"] = args ? args.extraConnectionAttributes : undefined;
            inputs["gcpMySQLSettings"] = args ? args.gcpMySQLSettings : undefined;
            inputs["ibmDb2Settings"] = args ? args.ibmDb2Settings : undefined;
            inputs["kafkaSettings"] = args ? args.kafkaSettings : undefined;
            inputs["kinesisSettings"] = args ? args.kinesisSettings : undefined;
            inputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            inputs["microsoftSqlServerSettings"] = args ? args.microsoftSqlServerSettings : undefined;
            inputs["mongoDbSettings"] = args ? args.mongoDbSettings : undefined;
            inputs["mySqlSettings"] = args ? args.mySqlSettings : undefined;
            inputs["neptuneSettings"] = args ? args.neptuneSettings : undefined;
            inputs["oracleSettings"] = args ? args.oracleSettings : undefined;
            inputs["password"] = args ? args.password : undefined;
            inputs["port"] = args ? args.port : undefined;
            inputs["postgreSqlSettings"] = args ? args.postgreSqlSettings : undefined;
            inputs["redisSettings"] = args ? args.redisSettings : undefined;
            inputs["redshiftSettings"] = args ? args.redshiftSettings : undefined;
            inputs["resourceIdentifier"] = args ? args.resourceIdentifier : undefined;
            inputs["s3Settings"] = args ? args.s3Settings : undefined;
            inputs["serverName"] = args ? args.serverName : undefined;
            inputs["sslMode"] = args ? args.sslMode : undefined;
            inputs["sybaseSettings"] = args ? args.sybaseSettings : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["username"] = args ? args.username : undefined;
            inputs["externalId"] = undefined /*out*/;
        } else {
            inputs["certificateArn"] = undefined /*out*/;
            inputs["databaseName"] = undefined /*out*/;
            inputs["docDbSettings"] = undefined /*out*/;
            inputs["dynamoDbSettings"] = undefined /*out*/;
            inputs["elasticsearchSettings"] = undefined /*out*/;
            inputs["endpointIdentifier"] = undefined /*out*/;
            inputs["endpointType"] = undefined /*out*/;
            inputs["engineName"] = undefined /*out*/;
            inputs["externalId"] = undefined /*out*/;
            inputs["extraConnectionAttributes"] = undefined /*out*/;
            inputs["gcpMySQLSettings"] = undefined /*out*/;
            inputs["ibmDb2Settings"] = undefined /*out*/;
            inputs["kafkaSettings"] = undefined /*out*/;
            inputs["kinesisSettings"] = undefined /*out*/;
            inputs["kmsKeyId"] = undefined /*out*/;
            inputs["microsoftSqlServerSettings"] = undefined /*out*/;
            inputs["mongoDbSettings"] = undefined /*out*/;
            inputs["mySqlSettings"] = undefined /*out*/;
            inputs["neptuneSettings"] = undefined /*out*/;
            inputs["oracleSettings"] = undefined /*out*/;
            inputs["password"] = undefined /*out*/;
            inputs["port"] = undefined /*out*/;
            inputs["postgreSqlSettings"] = undefined /*out*/;
            inputs["redisSettings"] = undefined /*out*/;
            inputs["redshiftSettings"] = undefined /*out*/;
            inputs["resourceIdentifier"] = undefined /*out*/;
            inputs["s3Settings"] = undefined /*out*/;
            inputs["serverName"] = undefined /*out*/;
            inputs["sslMode"] = undefined /*out*/;
            inputs["sybaseSettings"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["username"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Endpoint.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Endpoint resource.
 */
export interface EndpointArgs {
    certificateArn?: pulumi.Input<string>;
    databaseName?: pulumi.Input<string>;
    docDbSettings?: pulumi.Input<inputs.dms.EndpointDocDbSettingsArgs>;
    dynamoDbSettings?: pulumi.Input<inputs.dms.EndpointDynamoDbSettingsArgs>;
    elasticsearchSettings?: pulumi.Input<inputs.dms.EndpointElasticsearchSettingsArgs>;
    endpointIdentifier?: pulumi.Input<string>;
    endpointType: pulumi.Input<string>;
    engineName: pulumi.Input<string>;
    extraConnectionAttributes?: pulumi.Input<string>;
    gcpMySQLSettings?: pulumi.Input<inputs.dms.EndpointGcpMySQLSettingsArgs>;
    ibmDb2Settings?: pulumi.Input<inputs.dms.EndpointIbmDb2SettingsArgs>;
    kafkaSettings?: pulumi.Input<inputs.dms.EndpointKafkaSettingsArgs>;
    kinesisSettings?: pulumi.Input<inputs.dms.EndpointKinesisSettingsArgs>;
    kmsKeyId?: pulumi.Input<string>;
    microsoftSqlServerSettings?: pulumi.Input<inputs.dms.EndpointMicrosoftSqlServerSettingsArgs>;
    mongoDbSettings?: pulumi.Input<inputs.dms.EndpointMongoDbSettingsArgs>;
    mySqlSettings?: pulumi.Input<inputs.dms.EndpointMySqlSettingsArgs>;
    neptuneSettings?: pulumi.Input<inputs.dms.EndpointNeptuneSettingsArgs>;
    oracleSettings?: pulumi.Input<inputs.dms.EndpointOracleSettingsArgs>;
    password?: pulumi.Input<string>;
    port?: pulumi.Input<number>;
    postgreSqlSettings?: pulumi.Input<inputs.dms.EndpointPostgreSqlSettingsArgs>;
    redisSettings?: pulumi.Input<inputs.dms.EndpointRedisSettingsArgs>;
    redshiftSettings?: pulumi.Input<inputs.dms.EndpointRedshiftSettingsArgs>;
    resourceIdentifier?: pulumi.Input<string>;
    s3Settings?: pulumi.Input<inputs.dms.EndpointS3SettingsArgs>;
    serverName?: pulumi.Input<string>;
    sslMode?: pulumi.Input<string>;
    sybaseSettings?: pulumi.Input<inputs.dms.EndpointSybaseSettingsArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.dms.EndpointTagArgs>[]>;
    username?: pulumi.Input<string>;
}
